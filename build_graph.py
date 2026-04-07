"""Build the knowledge graph (wiki/graph.json) from wiki article frontmatter.

Scans all markdown files in wiki/<source-slug>/ folders, parses YAML
frontmatter, and outputs a JSON graph of nodes and edges.

Usage:
    uv run python build_graph.py
"""

import json
import logging
import os
import re
import sys
from pathlib import Path


# Configure logging with basicConfig
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s,p%(process)s,{%(filename)s:%(lineno)d},%(levelname)s,%(message)s",
)

logger = logging.getLogger(__name__)

WIKI_DIR = "wiki"
OUTPUT_JSON = "wiki/graph.json"
OUTPUT_HTML = "wiki/graph.html"


def _parse_frontmatter(file_path: str) -> dict:
    """Parse YAML frontmatter from a markdown file.

    Returns a dict with frontmatter fields, or empty dict if no frontmatter.
    """
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            content = f.read()
    except (OSError, UnicodeDecodeError) as e:
        logger.warning(f"Could not read {file_path}: {e}")
        return {}

    if not content.startswith("---"):
        return {}

    end_match = content.find("---", 3)
    if end_match == -1:
        return {}

    frontmatter_text = content[3:end_match].strip()
    result = {}

    for line in frontmatter_text.split("\n"):
        line = line.strip()
        if not line or ":" not in line:
            continue

        key, _, value = line.partition(":")
        key = key.strip()
        value = value.strip()

        if value.startswith("[") and value.endswith("]"):
            items = value[1:-1]
            result[key] = [
                item.strip().strip('"').strip("'")
                for item in items.split(",")
                if item.strip()
            ]
        elif value.startswith('"') and value.endswith('"'):
            result[key] = value[1:-1]
        elif value.startswith("'") and value.endswith("'"):
            result[key] = value[1:-1]
        else:
            result[key] = value

    return result


def _extract_related_ids(
    frontmatter: dict,
    source_folder: str,
) -> list:
    """Extract related article IDs from frontmatter related field.

    The related field may be a list of items or a single string.
    Each item contains one or more markdown links like [name](file.md).
    Also handles relative paths like ../other-folder/file.md.
    """
    related_raw = frontmatter.get("related", [])
    if isinstance(related_raw, str):
        related_raw = [related_raw]

    full_text = " ".join(related_raw)
    link_matches = re.findall(r'\(([^)]+\.md)\)', full_text)

    related_ids = []
    for path in link_matches:
        if path.startswith("../"):
            parts = path.split("/")
            folder = parts[1] if len(parts) > 2 else source_folder
            filename = parts[-1]
        else:
            folder = source_folder
            filename = path

        article_id = f"{folder}/{filename.replace('.md', '')}"
        related_ids.append(article_id)

    return related_ids


def _determine_node_type(filename: str) -> str:
    """Determine if a file is a summary or article based on filename."""
    if filename.startswith("summary-") or filename == "summary.md":
        return "summary"
    return "article"


def _scan_wiki_folders() -> list:
    """Scan wiki/ for source folders and their markdown files.

    Returns list of (source_folder, filename, full_path) tuples.
    """
    wiki_path = Path(WIKI_DIR)
    results = []

    for folder in sorted(wiki_path.iterdir()):
        if not folder.is_dir():
            continue

        for md_file in sorted(folder.glob("*.md")):
            results.append((folder.name, md_file.name, str(md_file)))

    logger.info(f"Found {len(results)} markdown files in wiki/ folders")
    return results


def _build_nodes(
    files: list,
) -> list:
    """Build node list from scanned wiki files."""
    nodes = []

    for source_folder, filename, full_path in files:
        frontmatter = _parse_frontmatter(full_path)
        node_type = _determine_node_type(filename)
        article_id = f"{source_folder}/{filename.replace('.md', '')}"

        title = frontmatter.get("title", filename.replace(".md", "").replace("-", " ").title())

        tags = frontmatter.get("tags", [])
        if isinstance(tags, str):
            tags = [t.strip() for t in tags.split(",")]

        node = {
            "id": article_id,
            "title": title,
            "file": f"wiki/{source_folder}/{filename}",
            "tags": tags,
            "source_folder": source_folder,
            "type": node_type,
        }
        nodes.append(node)

    logger.info(f"Built {len(nodes)} nodes")
    return nodes


def _build_edges(
    files: list,
    node_ids: set,
) -> list:
    """Build edge list from article frontmatter relationships."""
    edges = []
    seen_edges = set()

    for source_folder, filename, full_path in files:
        node_type = _determine_node_type(filename)
        if node_type == "summary":
            continue

        article_id = f"{source_folder}/{filename.replace('.md', '')}"
        frontmatter = _parse_frontmatter(full_path)

        related_ids = _extract_related_ids(frontmatter, source_folder)
        for target_id in related_ids:
            if target_id in node_ids:
                edge_key = (article_id, target_id, "related")
                if edge_key not in seen_edges:
                    edges.append({
                        "source": article_id,
                        "target": target_id,
                        "type": "related",
                    })
                    seen_edges.add(edge_key)

        summary_candidates = [
            f"{source_folder}/summary-{source_folder}",
            f"{source_folder}/summary",
        ]
        for summary_id in summary_candidates:
            if summary_id in node_ids:
                edge_key = (article_id, summary_id, "source")
                if edge_key not in seen_edges:
                    edges.append({
                        "source": article_id,
                        "target": summary_id,
                        "type": "source",
                    })
                    seen_edges.add(edge_key)
                break

    logger.info(f"Built {len(edges)} edges")
    return edges


def build_graph() -> dict:
    """Build the complete knowledge graph from wiki articles."""
    files = _scan_wiki_folders()
    nodes = _build_nodes(files)
    node_ids = {node["id"] for node in nodes}
    edges = _build_edges(files, node_ids)

    return {"nodes": nodes, "edges": edges}


def _generate_html(
    graph_json: str,
) -> str:
    """Generate a self-contained HTML visualization with embedded graph data."""
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Knowledge Base Graph</title>
<style>
  * {{ margin: 0; padding: 0; box-sizing: border-box; }}

  body {{
    font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
    background: #0d1117;
    color: #c9d1d9;
    overflow: hidden;
  }}

  #controls {{
    position: fixed;
    top: 16px;
    left: 16px;
    z-index: 10;
    background: #161b22;
    border: 1px solid #30363d;
    border-radius: 8px;
    padding: 16px;
    max-width: 280px;
  }}

  #controls h2 {{
    font-size: 14px;
    margin-bottom: 12px;
    color: #f0f6fc;
  }}

  #controls label {{
    display: block;
    font-size: 12px;
    margin-bottom: 4px;
    color: #8b949e;
  }}

  #controls select, #controls input {{
    width: 100%;
    padding: 6px 8px;
    margin-bottom: 10px;
    background: #0d1117;
    border: 1px solid #30363d;
    border-radius: 4px;
    color: #c9d1d9;
    font-size: 12px;
  }}

  .legend {{
    margin-top: 12px;
    font-size: 11px;
  }}

  .legend-item {{
    display: flex;
    align-items: center;
    margin-bottom: 4px;
  }}

  .legend-dot {{
    width: 10px;
    height: 10px;
    border-radius: 50%;
    margin-right: 8px;
    flex-shrink: 0;
  }}

  #tooltip {{
    position: fixed;
    background: #161b22;
    border: 1px solid #30363d;
    border-radius: 6px;
    padding: 10px 14px;
    font-size: 12px;
    pointer-events: none;
    opacity: 0;
    transition: opacity 0.15s;
    max-width: 300px;
    z-index: 20;
  }}

  #tooltip .title {{
    font-weight: 600;
    color: #f0f6fc;
    margin-bottom: 4px;
  }}

  #tooltip .tags {{
    color: #8b949e;
    margin-top: 4px;
  }}

  #tooltip .tag {{
    display: inline-block;
    background: #1f2937;
    border-radius: 3px;
    padding: 1px 6px;
    margin: 2px 2px 2px 0;
    font-size: 10px;
    color: #79c0ff;
  }}

  #stats {{
    position: fixed;
    bottom: 16px;
    left: 16px;
    font-size: 11px;
    color: #484f58;
    z-index: 10;
  }}
</style>
</head>
<body>

<div id="controls">
  <h2>Knowledge Graph</h2>

  <label for="filter-folder">Source folder</label>
  <select id="filter-folder">
    <option value="all">All folders</option>
  </select>

  <label for="filter-tag">Tag</label>
  <select id="filter-tag">
    <option value="all">All tags</option>
  </select>

  <label for="edge-type">Edge type</label>
  <select id="edge-type">
    <option value="all">All edges</option>
    <option value="related">Related only</option>
    <option value="source">Source only</option>
  </select>

  <div class="legend">
    <div class="legend-item"><div class="legend-dot" style="background:#f78166"></div> Article</div>
    <div class="legend-item"><div class="legend-dot" style="background:#3fb950"></div> Summary</div>
    <div class="legend-item"><div class="legend-dot" style="background:#30363d; border:1px dashed #484f58"></div> Filtered out</div>
  </div>
</div>

<div id="tooltip">
  <div class="title"></div>
  <div class="folder"></div>
  <div class="tags"></div>
</div>

<div id="stats"></div>

<svg id="graph"></svg>

<script src="https://d3js.org/d3.v7.min.js"></script>
<script>
(function() {{
  const data = {graph_json};

  const svg = d3.select("#graph");
  const width = window.innerWidth;
  const height = window.innerHeight;
  svg.attr("width", width).attr("height", height);

  const folders = [...new Set(data.nodes.map(n => n.source_folder))].sort();
  const allTags = [...new Set(data.nodes.flatMap(n => n.tags || []))].sort();

  const folderSelect = document.getElementById("filter-folder");
  folders.forEach(f => {{
    const opt = document.createElement("option");
    opt.value = f;
    opt.textContent = f;
    folderSelect.appendChild(opt);
  }});

  const tagSelect = document.getElementById("filter-tag");
  allTags.forEach(t => {{
    const opt = document.createElement("option");
    opt.value = t;
    opt.textContent = t;
    tagSelect.appendChild(opt);
  }});

  const folderColors = {{}};
  const palette = ["#f78166", "#d2a8ff", "#79c0ff", "#56d364", "#ffa657", "#ff7b72", "#a5d6ff"];
  folders.forEach((f, i) => {{ folderColors[f] = palette[i % palette.length]; }});

  const simulation = d3.forceSimulation(data.nodes)
    .force("link", d3.forceLink(data.edges).id(d => d.id).distance(100))
    .force("charge", d3.forceManyBody().strength(-300))
    .force("center", d3.forceCenter(width / 2, height / 2))
    .force("collision", d3.forceCollide().radius(30));

  const g = svg.append("g");

  svg.call(d3.zoom()
    .scaleExtent([0.2, 4])
    .on("zoom", (event) => g.attr("transform", event.transform)));

  const link = g.append("g")
    .selectAll("line")
    .data(data.edges)
    .join("line")
    .attr("stroke", d => d.type === "source" ? "#238636" : "#30363d")
    .attr("stroke-width", d => d.type === "source" ? 1.5 : 1)
    .attr("stroke-dasharray", d => d.type === "source" ? "4,3" : null);

  const node = g.append("g")
    .selectAll("circle")
    .data(data.nodes)
    .join("circle")
    .attr("r", d => d.type === "summary" ? 10 : 7)
    .attr("fill", d => d.type === "summary" ? "#3fb950" : folderColors[d.source_folder])
    .attr("stroke", "#0d1117")
    .attr("stroke-width", 1.5)
    .style("cursor", "pointer")
    .call(d3.drag()
      .on("start", dragstarted)
      .on("drag", dragged)
      .on("end", dragended));

  const label = g.append("g")
    .selectAll("text")
    .data(data.nodes)
    .join("text")
    .text(d => d.title.length > 30 ? d.title.slice(0, 28) + "..." : d.title)
    .attr("font-size", 10)
    .attr("fill", "#8b949e")
    .attr("dx", 14)
    .attr("dy", 4);

  const tooltip = document.getElementById("tooltip");

  node.on("mouseover", (event, d) => {{
    tooltip.querySelector(".title").textContent = d.title;
    tooltip.querySelector(".folder").textContent = "Folder: " + d.source_folder;
    const tagsHtml = (d.tags || []).map(t => `<span class="tag">${{t}}</span>`).join("");
    tooltip.querySelector(".tags").innerHTML = tagsHtml;
    tooltip.style.opacity = 1;
    tooltip.style.left = (event.clientX + 16) + "px";
    tooltip.style.top = (event.clientY - 10) + "px";

    const connected = new Set();
    data.edges.forEach(e => {{
      const sid = typeof e.source === "object" ? e.source.id : e.source;
      const tid = typeof e.target === "object" ? e.target.id : e.target;
      if (sid === d.id) connected.add(tid);
      if (tid === d.id) connected.add(sid);
    }});
    connected.add(d.id);

    node.attr("opacity", n => connected.has(n.id) ? 1 : 0.15);
    label.attr("opacity", n => connected.has(n.id) ? 1 : 0.1);
    link.attr("opacity", e => {{
      const sid = typeof e.source === "object" ? e.source.id : e.source;
      const tid = typeof e.target === "object" ? e.target.id : e.target;
      return (sid === d.id || tid === d.id) ? 1 : 0.05;
    }});
  }})
  .on("mousemove", (event) => {{
    tooltip.style.left = (event.clientX + 16) + "px";
    tooltip.style.top = (event.clientY - 10) + "px";
  }})
  .on("mouseout", () => {{
    tooltip.style.opacity = 0;
    node.attr("opacity", 1);
    label.attr("opacity", 1);
    link.attr("opacity", 1);
  }});

  simulation.on("tick", () => {{
    link
      .attr("x1", d => d.source.x)
      .attr("y1", d => d.source.y)
      .attr("x2", d => d.target.x)
      .attr("y2", d => d.target.y);
    node
      .attr("cx", d => d.x)
      .attr("cy", d => d.y);
    label
      .attr("x", d => d.x)
      .attr("y", d => d.y);
  }});

  const articleCount = data.nodes.filter(n => n.type === "article").length;
  const summaryCount = data.nodes.filter(n => n.type === "summary").length;
  const edgeCount = data.edges.length;
  document.getElementById("stats").textContent =
    `${{articleCount}} articles | ${{summaryCount}} summaries | ${{edgeCount}} edges | ${{allTags.length}} tags`;

  function applyFilters() {{
    const folder = folderSelect.value;
    const tag = tagSelect.value;
    const edgeType = document.getElementById("edge-type").value;

    const activeNodes = new Set();
    data.nodes.forEach(n => {{
      const folderMatch = folder === "all" || n.source_folder === folder;
      const tagMatch = tag === "all" || (n.tags || []).includes(tag);
      if (folderMatch && tagMatch) activeNodes.add(n.id);
    }});

    node
      .attr("fill", d => {{
        if (!activeNodes.has(d.id)) return "#21262d";
        return d.type === "summary" ? "#3fb950" : folderColors[d.source_folder];
      }})
      .attr("opacity", d => activeNodes.has(d.id) ? 1 : 0.2)
      .attr("r", d => {{
        if (!activeNodes.has(d.id)) return 4;
        return d.type === "summary" ? 10 : 7;
      }});

    label.attr("opacity", d => activeNodes.has(d.id) ? 1 : 0.1);

    link
      .attr("opacity", d => {{
        const sid = typeof d.source === "object" ? d.source.id : d.source;
        const tid = typeof d.target === "object" ? d.target.id : d.target;
        const nodesVisible = activeNodes.has(sid) && activeNodes.has(tid);
        const typeMatch = edgeType === "all" || d.type === edgeType;
        return (nodesVisible && typeMatch) ? 0.6 : 0.03;
      }});
  }}

  folderSelect.addEventListener("change", applyFilters);
  tagSelect.addEventListener("change", applyFilters);
  document.getElementById("edge-type").addEventListener("change", applyFilters);

  function dragstarted(event) {{
    if (!event.active) simulation.alphaTarget(0.3).restart();
    event.subject.fx = event.subject.x;
    event.subject.fy = event.subject.y;
  }}

  function dragged(event) {{
    event.subject.fx = event.x;
    event.subject.fy = event.y;
  }}

  function dragended(event) {{
    if (!event.active) simulation.alphaTarget(0);
    event.subject.fx = null;
    event.subject.fy = null;
  }}
}})();
</script>
</body>
</html>"""


def main():
    """Build graph.json and graph.html from wiki article frontmatter."""
    logger.info("Building knowledge graph from wiki/ articles...")

    graph = build_graph()
    graph_json = json.dumps(graph, indent=2)

    with open(OUTPUT_JSON, "w", encoding="utf-8") as f:
        f.write(graph_json)

    html_content = _generate_html(graph_json)
    with open(OUTPUT_HTML, "w", encoding="utf-8") as f:
        f.write(html_content)

    article_count = sum(1 for n in graph["nodes"] if n["type"] == "article")
    summary_count = sum(1 for n in graph["nodes"] if n["type"] == "summary")
    related_count = sum(1 for e in graph["edges"] if e["type"] == "related")
    source_count = sum(1 for e in graph["edges"] if e["type"] == "source")

    logger.info(
        f"Wrote {OUTPUT_JSON} and {OUTPUT_HTML}: "
        f"{article_count} articles, {summary_count} summaries, "
        f"{related_count} related edges, {source_count} source edges"
    )


if __name__ == "__main__":
    main()

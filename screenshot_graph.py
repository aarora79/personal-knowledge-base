"""Take a screenshot of wiki/graph.html and save it to docs/img/kg.png."""
import logging
import os

from playwright.sync_api import sync_playwright


# Configure logging with basicConfig
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s,p%(process)s,{%(filename)s:%(lineno)d},%(levelname)s,%(message)s",
)

logger = logging.getLogger(__name__)

GRAPH_HTML = "wiki/graph.html"
OUTPUT_PNG = "docs/img/kg.png"
VIEWPORT_WIDTH = 1400
VIEWPORT_HEIGHT = 900
SETTLE_TIME_MS = 4000


def _take_screenshot(
    html_path: str,
    output_path: str,
    width: int,
    height: int,
    settle_ms: int,
) -> None:
    """Launch headless browser and screenshot the graph HTML."""
    abs_html = os.path.abspath(html_path)
    abs_output = os.path.abspath(output_path)

    os.makedirs(os.path.dirname(abs_output), exist_ok=True)

    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page(viewport={"width": width, "height": height})
        page.goto(f"file://{abs_html}")
        page.wait_for_timeout(settle_ms)
        page.screenshot(path=abs_output, full_page=False)
        browser.close()

    logger.info("Saved graph screenshot to %s", abs_output)


def main() -> None:
    """Take a screenshot of the knowledge graph."""
    if not os.path.exists(GRAPH_HTML):
        logger.error("Graph HTML not found at %s. Run build_graph.py first.", GRAPH_HTML)
        return

    _take_screenshot(
        html_path=GRAPH_HTML,
        output_path=OUTPUT_PNG,
        width=VIEWPORT_WIDTH,
        height=VIEWPORT_HEIGHT,
        settle_ms=SETTLE_TIME_MS,
    )


if __name__ == "__main__":
    main()

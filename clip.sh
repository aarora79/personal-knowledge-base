#!/bin/bash
# clip.sh - Clip a URL into raw/ as a markdown file
#
# Usage:
#   ./clip.sh <url> [slug]
#   ./clip.sh --bulk urls.txt          # Bulk clip from file
#
# Tools (tried in order):
#   1. markitdown:  Tried first (handles PDFs, DOCX, YouTube, web)
#   2. trafilatura: Fallback for web articles/blog posts
#
# Install:
#   uv sync

set -e

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
RAW_DIR="$SCRIPT_DIR/raw"
DATE_PREFIX=$(date +%Y%m%d)

_generate_slug() {
    echo "$1" | sed 's|https\?://||;s|www\.||;s|/|-|g;s|[^a-zA-Z0-9-]||g' | cut -c1-60
}


_clip_with_trafilatura() {
    local url="$1"
    local slug="$2"
    local outfile="$RAW_DIR/${DATE_PREFIX}-${slug}.md"

    echo "Clipping with trafilatura: $url"
    uv run trafilatura -u "$url" --output-format markdown > "$outfile"

    if [ -s "$outfile" ]; then
        echo "Saved to: $outfile"
    else
        echo "Warning: trafilatura returned empty content for $url"
        rm -f "$outfile"
        return 1
    fi
}


_clip_with_markitdown() {
    local url="$1"
    local slug="$2"
    local outfile="$RAW_DIR/${DATE_PREFIX}-${slug}.md"

    echo "Clipping with markitdown: $url"
    uv run markitdown "$url" > "$outfile"

    if [ -s "$outfile" ]; then
        echo "Saved to: $outfile"
    else
        echo "Warning: markitdown returned empty content for $url"
        rm -f "$outfile"
        return 1
    fi
}


_bulk_clip() {
    local file="$1"

    if [ ! -f "$file" ]; then
        echo "Error: File not found: $file"
        exit 1
    fi

    while IFS= read -r url; do
        # Skip empty lines and comments
        [[ -z "$url" || "$url" == \#* ]] && continue

        slug=$(_generate_slug "$url")
        _clip_with_markitdown "$url" "$slug" || _clip_with_trafilatura "$url" "$slug" || true
        sleep 1  # be polite to servers
    done < "$file"

    echo "Done. Files in $RAW_DIR/"
}


clip() {
    local url=""
    local slug=""

    # Parse arguments
    while [[ $# -gt 0 ]]; do
        case "$1" in
            --pdf|--youtube|--markitdown)
                # Kept for backwards compatibility, but markitdown is now always tried first
                shift
                ;;
            --bulk)
                _bulk_clip "$2"
                return
                ;;
            *)
                if [ -z "$url" ]; then
                    url="$1"
                else
                    slug="$1"
                fi
                shift
                ;;
        esac
    done

    if [ -z "$url" ]; then
        echo "Usage: ./clip.sh <url> [slug]"
        echo "       ./clip.sh --pdf <url> [slug]"
        echo "       ./clip.sh --youtube <url> [slug]"
        echo "       ./clip.sh --bulk urls.txt"
        exit 1
    fi

    # Auto-generate slug if not provided
    if [ -z "$slug" ]; then
        slug=$(_generate_slug "$url")
    fi

    # Try markitdown first, fall back to trafilatura
    if _clip_with_markitdown "$url" "$slug"; then
        return 0
    fi

    echo "markitdown failed, trying trafilatura..."
    _clip_with_trafilatura "$url" "$slug"
}

# Run
clip "$@"

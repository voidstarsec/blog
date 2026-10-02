#!/bin/bash
set -e

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cd "$SCRIPT_DIR"

# Activate the virtual environment
source pelican-venv/bin/activate

# Build the site with the bootstrap3 theme
pelican content -o output/ -s pelicanconf.py -t /home/wrongbaud/projects/vss/blog-resources/pelican-themes/pelican-bootstrap3

# Post-process HTML (table classes, image styling)
bash ./prep.sh

# Copy custom CSS
cp vss-style.css output/theme/css/style.css

echo "Build complete."

if [ "$1" = "--deploy" ]; then
    echo "Deploying to gh-pages..."

    # Images (assets/) and some older pages only exist on gh-pages, not in
    # content/. ghp-import replaces the whole branch with output/, so copy
    # anything live that the build didn't produce back in first.
    git fetch origin gh-pages
    LIVE_DIR="$(mktemp -d)"
    trap 'rm -rf "$LIVE_DIR"' EXIT
    git archive origin/gh-pages | tar -x -C "$LIVE_DIR"
    rsync -a --ignore-existing "$LIVE_DIR"/ output/

    ghp-import output/ -b gh-pages -r origin -p -n
    echo "Deployed to gh-pages branch."
else
    echo "Run 'make serve' to preview locally, or './build.sh --deploy' to push to gh-pages."
fi

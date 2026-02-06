#!/bin/bash
# Fix formatting and auto-fixable lint issues (e.g. unused imports). Run before pushing.
# Install dev deps first: uv sync --extra dev
set -e
cd "$(dirname "$0")/.."

echo "Formatting code..."
uv run ruff format .

echo "Fixing auto-fixable lint issues (e.g. unused imports)..."
uv run ruff check . --fix

echo "✓ Format and fix done."

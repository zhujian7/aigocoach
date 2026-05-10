#!/usr/bin/env bash
set -euo pipefail

REPO_ROOT="$(cd "$(dirname "$0")/.." && pwd)"
TEMPLATES_DIR="$REPO_ROOT/templates"

# Determine round number: argument > .aigocoach.yaml > default 1
if [ $# -ge 1 ]; then
    ROUND="$1"
else
    ROUND=$(grep 'current_round:' "$REPO_ROOT/.aigocoach.yaml" 2>/dev/null | awk '{print $2}' || echo "1")
fi

ROUND_DIR="$REPO_ROOT/my-progress/round-${ROUND}"

echo "=== AIgoCoach — Round $ROUND ==="

if [ -d "$ROUND_DIR" ]; then
    echo "my-progress/round-${ROUND}/ already exists."
    read -p "Overwrite and start fresh? (y/N) " -n 1 -r
    echo ""
    if [[ ! $REPLY =~ ^[Yy]$ ]]; then
        echo "Aborted."
        exit 0
    fi
    rm -rf "$ROUND_DIR"
fi

echo "Initializing my-progress/round-${ROUND}/ from templates..."
mkdir -p "$ROUND_DIR"

# Copy checklist (per-round)
cp "$TEMPLATES_DIR/checklist.md" "$ROUND_DIR/checklist.md"

# Copy progress.md to my-progress/ only if it doesn't exist yet (shared across rounds)
PROGRESS_FILE="$REPO_ROOT/my-progress/progress.md"
if [ ! -f "$PROGRESS_FILE" ]; then
    cp "$TEMPLATES_DIR/progress.md" "$PROGRESS_FILE"
    echo "Created my-progress/progress.md (shared across all rounds)"
fi

# Copy problem stubs, tests, solutions, and READMEs
echo "Copying problem files..."
cd "$TEMPLATES_DIR/problems"
find . -type d | while read -r dir; do
    mkdir -p "$ROUND_DIR/problems/$dir"
done

find . -name "*.go" -o -name "*.py" -o -name "README.md" -o -name "README_zh.md" \
    | while read -r file; do
    cp "$file" "$ROUND_DIR/problems/$file"
done

# Copy assets if any
find . -path "*/assets/*" -type f 2>/dev/null | while read -r file; do
    cp "$file" "$ROUND_DIR/problems/$file"
done

# Update current_round in .aigocoach.yaml
sed -i '' "s/^current_round:.*/current_round: ${ROUND}/" "$REPO_ROOT/.aigocoach.yaml"

echo ""
echo "Done! Your workspace is ready at my-progress/round-${ROUND}/"
echo ""
echo "  my-progress/round-${ROUND}/"
echo "  ├── checklist.md   — your problem checklist (per round)"
echo "  └── problems/      — write your solutions here"
echo ""
echo "  my-progress/progress.md — your progress tracker (shared across all rounds)"
echo ""
echo "Start a new round:   ./scripts/init.sh <round-number>"
echo "Go solutions:      templates/problems/<category>/<problem>/solution.go"
echo "Python solutions:  templates/problems/<category>/<problem>/solution.py"
echo "Problem info:      templates/problems/<category>/<problem>/README.md"
echo ""
echo "Test commands:"
echo "  Go:     go test ./my-progress/round-${ROUND}/problems/<category>/<problem>/... -v"
echo "  Python: pytest my-progress/round-${ROUND}/problems/<category>/<problem>/ -v"
echo ""
echo "This directory is gitignored — it's your personal workspace."

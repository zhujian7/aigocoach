# AIgoCoach 🤖

English | [中文](README_zh.md)

> Your AI algorithm coach — 150 classic problems in Go & Python, guided step by step.

## What Is This?

An interview prep repo designed to work with AI coding assistants (Claude Code, Cursor, Windsurf, etc.). Clone it, open it, and start practicing algorithm problems with an AI coach that:

- Guides you through 150 problems (based on NeetCode 150) in Go and Python without giving away answers
- Tracks your progress in `my-progress/checklist.md`
- Records insights and mistakes in `my-progress/progress.md` and identifies weak areas
- Generates variant problems based on your error patterns
- Provides optimal reference solutions for every problem
- Supports both English and Chinese interaction

## Quick Start

```bash
git clone https://github.com/xuezhaojun/aigocoach.git
cd aigocoach

# Initialize your personal workspace
./scripts/init.sh

# (Optional) Set your preferred language
# Edit .aigocoach.yaml → language: "zh" or "en"

# Open in VS Code with Claude Code / Cursor / Windsurf
code .

# Start talking to the agent:
# "Let's start with an easy problem"
# "I want to practice binary search"
# "Show me my weak areas"
```

## How It Works

### 1. Pick a Problem

Open `my-progress/checklist.md` to see all 150 problems organized by category and difficulty (numbered `01.01`, `01.02`, etc.). Each links to your working Go and Python files.

### 2. Write Your Solution

Edit the `.go` or `.py` file in `my-progress/problems/` — the function signature is already there, just fill in the body. Choose whichever language you want to practice.

### 3. Run Tests

```bash
# Go — test a specific problem
go test ./my-progress/problems/01_arrays_hashing/03_two_sum/... -v

# Go — test all problems in a category
go test ./my-progress/problems/07_trees/... -v

# Python — test a specific problem
pytest my-progress/problems/01_arrays_hashing/03_two_sum/ -v

# Python — test all problems in a category
pytest my-progress/problems/07_trees/ -v
```

### 4. Track Progress

The agent automatically updates `my-progress/checklist.md` (checkboxes) and `my-progress/progress.md` (session log with insights, mistakes, and knowledge points) as you work.

### 5. Check Reference Solutions

Each problem has reference solutions in `templates/problems/<category>/<problem>/solution.go` (Go) and `solution.py` (Python). Ask the agent or read it directly when you're stuck.

### 6. Reset & Start Fresh

```bash
# Reset all progress and solutions to blank state
./scripts/reset.sh
```

## Project Structure

```
aigocoach/
├── CLAUDE.md                  # Agent behavior instructions
├── AGENTS.md                  # Symlink → CLAUDE.md (for other AI tools)
├── .aigocoach.yaml        # User configuration (gitignored, created by init.sh)
├── templates/                 # READ-ONLY (do not modify)
│   ├── checklist.md           # Problem checklist template
│   ├── progress.md            # Progress tracker template
│   └── problems/              # Problem stubs, tests, solutions, metadata
│       ├── 01_arrays_hashing/
│       │   ├── 01_contains_duplicate/
│       │   │   ├── contains_duplicate.go      # Go function stub
│       │   │   ├── contains_duplicate_test.go  # Go tests
│       │   │   ├── solution.go                 # Go reference solution
│       │   │   ├── contains_duplicate.py       # Python function stub
│       │   │   ├── test_contains_duplicate.py  # Python tests (pytest)
│       │   │   ├── solution.py                 # Python reference solution
│       │   │   └── README.md                   # Difficulty, topics, approach
│       │   └── ...
│       ├── 02_two_pointers/       # 5 problems
│       ├── 03_sliding_window/     # 6 problems
│       ├── 04_stack/              # 7 problems
│       ├── 05_binary_search/      # 7 problems
│       ├── 06_linked_list/        # 11 problems
│       ├── 07_trees/              # 15 problems
│       ├── 08_tries/              # 3 problems
│       ├── 09_heap/               # 7 problems
│       ├── 10_backtracking/       # 9 problems
│       ├── 11_graphs/             # 13 problems
│       ├── 12_advanced_graphs/    # 6 problems
│       ├── 13_dp_1d/              # 12 problems
│       ├── 14_dp_2d/              # 11 problems
│       ├── 15_greedy/             # 8 problems
│       ├── 16_intervals/          # 6 problems
│       ├── 17_math_geometry/      # 8 problems
│       └── 18_bit_manipulation/   # 7 problems
├── my-progress/               # Your personal workspace (gitignored)
│   ├── round-1/               # Round 1
│   │   ├── checklist.md       # Your problem checklist with progress
│   │   ├── progress.md        # Your progress tracker (insights, mistakes, stats)
│   │   └── problems/          # Your working copies (write solutions here)
│   ├── round-2/               # Round 2 (fresh copy)
│   └── ...
├── tmp/                       # Variant problems (gitignored)
└── scripts/
    ├── init.sh                # Initialize my-progress/ from templates
    └── reset.sh               # Reset to fresh state
```

## Configuration

`.aigocoach.yaml` is your personal configuration file (gitignored). It is automatically created when you run `./scripts/init.sh`. You can also create it manually:

```yaml
# Language for agent interaction: "en" or "zh"
language: en

# Current practice round (1, 2, 3, ...)
# Each round creates a fresh copy of all problems under my-progress/round-N/
current_round: 1
```

| Field | Description | Default |
|-------|-------------|---------|
| `language` | Agent interaction language. `"en"` for English, `"zh"` for Chinese. | `en` |
| `current_round` | Active practice round number. Determines which `my-progress/round-N/` directory the agent uses. Updated automatically by `./scripts/init.sh <N>`. | `1` |

### Multi-Round Practice

You can practice all 150 problems multiple times. Each round gets a fresh workspace:

```bash
# Start round 1 (default)
./scripts/init.sh

# Start round 2 (fresh copy of all problems)
./scripts/init.sh 2

# Start round 3
./scripts/init.sh 3
```

Each round is stored independently under `my-progress/round-N/` with its own checklist and progress tracker. Previous rounds are preserved so you can compare improvement over time.

## License

MIT

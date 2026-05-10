#!/usr/bin/env python3
"""Verify Python solutions pass their tests.

For each problem, temporarily copies solution.py over the stub file,
runs pytest, then restores the original stub.

Usage:
    python scripts/verify_solutions.py --all
    python scripts/verify_solutions.py --problem 01_arrays_hashing/02_valid_anagram
    python scripts/verify_solutions.py --all --summary
"""

import argparse
import re
import subprocess
import shutil
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
TEMPLATES_DIR = REPO_ROOT / "templates" / "problems"


def find_all_problems():
    problems = []
    for category in sorted(TEMPLATES_DIR.iterdir()):
        if not category.is_dir():
            continue
        for problem in sorted(category.iterdir()):
            if not problem.is_dir() or problem.name == "assets":
                continue
            problems.append(problem)
    return problems


def get_module_name(prob_dir):
    go_stubs = [
        f for f in prob_dir.iterdir()
        if f.suffix == ".go"
        and f.name != "solution.go"
        and "_test" not in f.name
        and f.name not in ("treenode.go", "listnode.go", "helpers_test.go",
                           "node.go", "trienode.go")
    ]
    return go_stubs[0].stem if go_stubs else None


def verify_problem(prob_dir, module_name, verbose=False):
    stub_path = prob_dir / f"{module_name}.py"
    solution_path = prob_dir / "solution.py"
    test_path = prob_dir / f"test_{module_name}.py"
    backup_path = prob_dir / f"{module_name}.py.bak"

    if not solution_path.exists() or not test_path.exists() or not stub_path.exists():
        return "skip", "missing files"

    shutil.copy2(stub_path, backup_path)
    try:
        sol_content = solution_path.read_text()
        stub_content = stub_path.read_text()

        stub_funcs = re.findall(r'^(?:def|class)\s+(\w+)', stub_content, re.MULTILINE)
        for name in stub_funcs:
            solve_name = f"solve_{name}"
            sol_name_pascal = f"Solve{name}"
            if solve_name in sol_content:
                sol_content = sol_content.replace(solve_name, name)
            elif sol_name_pascal in sol_content:
                sol_content = sol_content.replace(sol_name_pascal, name)

        stub_path.write_text(sol_content)
        result = subprocess.run(
            [sys.executable, "-m", "pytest", str(test_path), "-x", "-q", "--tb=short"],
            capture_output=True, text=True, timeout=30,
            cwd=str(prob_dir)
        )
        if result.returncode == 0:
            return "pass", ""
        else:
            output = result.stdout + result.stderr
            lines = [l for l in output.split('\n') if l.strip() and 'FAILED' in l or 'Error' in l]
            return "fail", '\n'.join(lines[:3]) if lines else output[-200:]
    except subprocess.TimeoutExpired:
        return "timeout", "test timed out (30s)"
    except Exception as e:
        return "error", str(e)
    finally:
        shutil.move(str(backup_path), str(stub_path))


def main():
    parser = argparse.ArgumentParser(description="Verify Python solutions")
    parser.add_argument("--all", action="store_true")
    parser.add_argument("--problem", type=str)
    parser.add_argument("--summary", action="store_true", help="Only show summary")
    args = parser.parse_args()

    if not args.all and not args.problem:
        parser.print_help()
        sys.exit(1)

    if args.problem:
        problems = [TEMPLATES_DIR / args.problem]
    else:
        problems = find_all_problems()

    passed = 0
    failed = 0
    skipped = 0
    failures = []

    for prob_dir in problems:
        rel = str(prob_dir.relative_to(TEMPLATES_DIR))
        module_name = get_module_name(prob_dir)
        if not module_name:
            skipped += 1
            continue

        status, msg = verify_problem(prob_dir, module_name)

        if status == "pass":
            passed += 1
            if not args.summary:
                print(f"  PASS  {rel}")
        elif status == "skip":
            skipped += 1
        elif status == "fail":
            failed += 1
            failures.append((rel, msg))
            if not args.summary:
                print(f"  FAIL  {rel}")
        elif status == "timeout":
            failed += 1
            failures.append((rel, msg))
            if not args.summary:
                print(f"  TIME  {rel}")
        else:
            failed += 1
            failures.append((rel, msg))
            if not args.summary:
                print(f"  ERR   {rel}")

    print(f"\nResults: {passed} passed, {failed} failed, {skipped} skipped (out of {len(problems)})")

    if failures:
        print(f"\nFailures ({len(failures)}):")
        for path, msg in failures:
            print(f"\n  {path}:")
            for line in msg.split('\n'):
                print(f"    {line}")


if __name__ == "__main__":
    main()

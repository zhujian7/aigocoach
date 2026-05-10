#!/usr/bin/env python3
"""Generate Python stubs, tests, and solution skeletons from Go templates.

Usage:
    python scripts/generate_python.py --all
    python scripts/generate_python.py --problem 01_arrays_hashing/03_two_sum
    python scripts/generate_python.py --all --skip-existing
    python scripts/generate_python.py --all --dry-run
"""

import argparse
import os
import re
import sys
import json
from pathlib import Path
from typing import Optional

REPO_ROOT = Path(__file__).resolve().parent.parent
TEMPLATES_DIR = REPO_ROOT / "templates" / "problems"

# Standard tree_node.py content for problems that use TreeNode
TREE_NODE_PY = '''from typing import Optional, List
from collections import deque


class TreeNode:
    def __init__(self, val: int = 0, left: 'TreeNode' = None, right: 'TreeNode' = None):
        self.val = val
        self.left = left
        self.right = right


def build_tree(vals: List[int]) -> Optional[TreeNode]:
    if not vals or vals[0] == -101:
        return None
    root = TreeNode(vals[0])
    queue = deque([root])
    i = 1
    while queue and i < len(vals):
        node = queue.popleft()
        if i < len(vals) and vals[i] != -101:
            node.left = TreeNode(vals[i])
            queue.append(node.left)
        i += 1
        if i < len(vals) and vals[i] != -101:
            node.right = TreeNode(vals[i])
            queue.append(node.right)
        i += 1
    return root


def tree_to_list(root: Optional[TreeNode]) -> List[int]:
    if not root:
        return []
    result = []
    queue = deque([root])
    while queue:
        node = queue.popleft()
        if node is None:
            result.append(-101)
        else:
            result.append(node.val)
            queue.append(node.left)
            queue.append(node.right)
    while result and result[-1] == -101:
        result.pop()
    return result
'''

# Standard list_node.py content for problems that use ListNode
LIST_NODE_PY = '''from typing import Optional, List


class ListNode:
    def __init__(self, val: int = 0, next: 'ListNode' = None):
        self.val = val
        self.next = next


def build_list(vals: Optional[List[int]]) -> Optional[ListNode]:
    if not vals:
        return None
    dummy = ListNode()
    cur = dummy
    for v in vals:
        cur.next = ListNode(v)
        cur = cur.next
    return dummy.next


def list_to_array(head: Optional[ListNode]) -> Optional[List[int]]:
    if head is None:
        return None
    result = []
    cur = head
    while cur:
        result.append(cur.val)
        cur = cur.next
    return result
'''

# Go type -> Python type mapping
TYPE_MAP = {
    "int": "int",
    "int32": "int",
    "int64": "int",
    "uint32": "int",
    "float64": "float",
    "float32": "float",
    "string": "str",
    "bool": "bool",
    "byte": "str",
    "[]int": "List[int]",
    "[]int32": "List[int]",
    "[]float64": "List[float]",
    "[]string": "List[str]",
    "[]byte": "str",
    "[][]int": "List[List[int]]",
    "[][]string": "List[List[str]]",
    "[][]byte": "List[List[str]]",
    "*TreeNode": "Optional[TreeNode]",
    "*ListNode": "Optional[ListNode]",
    "[]*ListNode": "List[Optional[ListNode]]",
    "[]*Node": "List[Optional[Node]]",
    "*Node": "Optional[Node]",
    "*RandomNode": "Optional[RandomNode]",
}

# Default return values for Python stubs
DEFAULT_RETURNS = {
    "int": "0",
    "float": "0.0",
    "str": '""',
    "bool": "False",
    "None": "",
    "List[int]": "[]",
    "List[float]": "[]",
    "List[str]": "[]",
    "List[List[int]]": "[]",
    "List[List[str]]": "[]",
    "Optional[TreeNode]": "None",
    "Optional[ListNode]": "None",
    "Optional[Node]": "None",
    "Optional[RandomNode]": "None",
    "List[Optional[ListNode]]": "[]",
}


def camel_to_snake(name: str) -> str:
    """Convert camelCase/PascalCase to snake_case."""
    result = re.sub(r'([A-Z]+)([A-Z][a-z])', r'\1_\2', name)
    result = re.sub(r'([a-z0-9])([A-Z])', r'\1_\2', result)
    return result.lower()


def go_type_to_python(go_type: str) -> str:
    """Convert a Go type string to Python type hint."""
    go_type = go_type.strip()
    if go_type in TYPE_MAP:
        return TYPE_MAP[go_type]
    if go_type.startswith("[]"):
        inner = go_type_to_python(go_type[2:])
        return f"List[{inner}]"
    if go_type.startswith("*"):
        inner = go_type[1:]
        return f"Optional[{inner}]"
    return go_type


def parse_go_func(line: str) -> Optional[dict]:
    """Parse a Go function signature line into components."""
    m = re.match(
        r'func\s+(\w+)\s*\(([^)]*)\)\s*(.*?)\s*\{',
        line.strip()
    )
    if not m:
        return None
    name = m.group(1)
    params_str = m.group(2).strip()
    returns_str = m.group(3).strip()

    params = []
    if params_str:
        for param in split_go_params(params_str):
            param = param.strip()
            if not param:
                continue
            parts = param.rsplit(" ", 1)
            if len(parts) == 2:
                pname, ptype = parts
                params.append((pname.strip(), ptype.strip()))

    return_type = None
    if returns_str:
        returns_str = returns_str.strip("()")
        if "," in returns_str:
            return_type = "tuple"
        else:
            return_type = returns_str.strip()

    return {
        "name": name,
        "params": params,
        "return_type": return_type,
    }


def parse_go_method(line: str) -> Optional[dict]:
    """Parse a Go method signature (with receiver) into components."""
    m = re.match(
        r'func\s+\(\w+\s+\*?(\w+)\)\s+(\w+)\s*\(([^)]*)\)\s*(.*?)\s*\{',
        line.strip()
    )
    if not m:
        return None
    receiver_type = m.group(1)
    name = m.group(2)
    params_str = m.group(3).strip()
    returns_str = m.group(4).strip()

    params = []
    if params_str:
        for param in split_go_params(params_str):
            param = param.strip()
            if not param:
                continue
            parts = param.rsplit(" ", 1)
            if len(parts) == 2:
                pname, ptype = parts
                params.append((pname.strip(), ptype.strip()))

    return_type = None
    if returns_str:
        returns_str = returns_str.strip("()")
        return_type = returns_str.strip()

    return {
        "receiver": receiver_type,
        "name": name,
        "params": params,
        "return_type": return_type,
    }


def split_go_params(params_str: str) -> list:
    """Split Go parameter string handling nested brackets."""
    parts = []
    depth = 0
    current = []
    for ch in params_str:
        if ch in "([{":
            depth += 1
            current.append(ch)
        elif ch in ")]}":
            depth -= 1
            current.append(ch)
        elif ch == "," and depth == 0:
            parts.append("".join(current))
            current = []
        else:
            current.append(ch)
    if current:
        parts.append("".join(current))
    return parts


def needs_typing_imports(params: list, return_type: Optional[str]) -> set:
    """Determine which typing imports are needed."""
    imports = set()
    all_types = [go_type_to_python(p[1]) for p in params]
    if return_type:
        all_types.append(go_type_to_python(return_type))

    for t in all_types:
        if "List[" in t:
            imports.add("List")
        if "Optional[" in t:
            imports.add("Optional")
        if "Dict[" in t:
            imports.add("Dict")
    return imports


def generate_stub(prob_dir: Path, module_name: str) -> str:
    """Generate a Python stub file from the Go stub."""
    go_stub = prob_dir / f"{module_name}.go"
    if not go_stub.exists():
        return ""

    content = go_stub.read_text()
    lines = content.split("\n")

    has_treenode = (prob_dir / "treenode.go").exists()
    has_listnode = (prob_dir / "listnode.go").exists()

    # Detect class-based vs function-based
    funcs = []
    methods = []
    struct_names = set()

    for line in lines:
        line_stripped = line.strip()
        struct_m = re.match(r'type\s+(\w+)\s+struct\s*\{?', line_stripped)
        if struct_m:
            sname = struct_m.group(1)
            if sname not in ("TreeNode", "ListNode", "TrieNode"):
                struct_names.add(sname)

        func_info = parse_go_func(line_stripped)
        if func_info:
            funcs.append(func_info)
            continue

        method_info = parse_go_method(line_stripped)
        if method_info:
            methods.append(method_info)

    # Structs with methods are classes; structs without methods are inline types
    class_names = set()
    for m in methods:
        if m["receiver"] in struct_names:
            class_names.add(m["receiver"])
    inline_types = [s for s in struct_names if s not in class_names]

    is_class = len(class_names) > 0

    # Build imports
    all_params = []
    all_returns = []
    for f in funcs:
        all_params.extend(f["params"])
        if f["return_type"]:
            all_returns.append(f["return_type"])
    for m in methods:
        all_params.extend(m["params"])
        if m["return_type"]:
            all_returns.append(m["return_type"])

    typing_imports = set()
    for _, ptype in all_params:
        py_type = go_type_to_python(ptype)
        if "List[" in py_type:
            typing_imports.add("List")
        if "Optional[" in py_type:
            typing_imports.add("Optional")
    for rtype in all_returns:
        py_type = go_type_to_python(rtype)
        if "List[" in py_type:
            typing_imports.add("List")
        if "Optional[" in py_type:
            typing_imports.add("Optional")

    output_lines = []

    # Imports
    if typing_imports:
        output_lines.append(f"from typing import {', '.join(sorted(typing_imports))}")
    if has_treenode:
        output_lines.append("from tree_node import TreeNode")
    if has_listnode:
        output_lines.append("from list_node import ListNode")
    if output_lines:
        output_lines.append("")
        output_lines.append("")

    if is_class:
        # Generate class-based stub
        for sname in sorted(class_names):
            py_class_name = sname
            output_lines.append(f"class {py_class_name}:")

            # Find constructor and methods for this class
            class_methods = [m for m in methods if m["receiver"] == sname]
            constructors = [f for f in funcs
                            if f["name"].startswith("New") or f["name"] == "Constructor"
                            or f["name"].startswith("Constructor")]

            # __init__
            constructor = None
            for c in constructors:
                if sname.lower() in c["name"].lower() or len(constructors) == 1:
                    constructor = c
                    break
            if not constructor and constructors:
                constructor = constructors[0]

            if constructor:
                init_params = []
                for pname, ptype in constructor["params"]:
                    py_type = go_type_to_python(ptype)
                    init_params.append(f"{camel_to_snake(pname)}: {py_type}")
                params_str = ", ".join(["self"] + init_params)
                output_lines.append(f"    def __init__({params_str}):")
                output_lines.append("        pass")
            else:
                output_lines.append("    def __init__(self):")
                output_lines.append("        pass")

            # Other methods
            for m in class_methods:
                output_lines.append("")
                method_name = camel_to_snake(m["name"])
                mparams = []
                for pname, ptype in m["params"]:
                    py_type = go_type_to_python(ptype)
                    py_name = camel_to_snake(pname)
                    if py_name == "self":
                        py_name = "self_"
                    mparams.append(f"{py_name}: {py_type}")
                params_str = ", ".join(["self"] + mparams)

                ret_type = ""
                if m["return_type"]:
                    ret_type = f" -> {go_type_to_python(m['return_type'])}"
                else:
                    ret_type = " -> None"
                output_lines.append(f"    def {method_name}({params_str}){ret_type}:")
                output_lines.append("        pass")

            output_lines.append("")

        # Also generate standalone functions that aren't constructors
        non_constructor_funcs = [
            f for f in funcs
            if not f["name"].startswith("New")
            and f["name"] != "Constructor"
            and not f["name"].startswith("Constructor")
        ]
        for f in non_constructor_funcs:
            py_name = camel_to_snake(f["name"])
            fparams = []
            for pname, ptype in f["params"]:
                py_type = go_type_to_python(ptype)
                fparams.append(f"{camel_to_snake(pname)}: {py_type}")
            params_str = ", ".join(fparams)

            ret_annotation = ""
            if f["return_type"]:
                ret_annotation = f" -> {go_type_to_python(f['return_type'])}"
            output_lines.append(f"def {py_name}({params_str}){ret_annotation}:")
            output_lines.append("    pass")
            output_lines.append("")
    else:
        # Generate inline type definitions (e.g., Node for clone_graph)
        for sname in inline_types:
            output_lines.append(generate_inline_class(sname, prob_dir))
            output_lines.append("")
            output_lines.append("")

        # Generate function-based stubs
        for f in funcs:
            py_name = camel_to_snake(f["name"])
            fparams = []
            for pname, ptype in f["params"]:
                py_type = go_type_to_python(ptype)
                py_pname = camel_to_snake(pname)
                if py_pname in ("list", "type", "input", "next", "hash", "map", "set"):
                    py_pname += "_"
                fparams.append(f"{py_pname}: {py_type}")
            params_str = ", ".join(fparams)

            ret_annotation = ""
            if f["return_type"]:
                ret_annotation = f" -> {go_type_to_python(f['return_type'])}"
            else:
                ret_annotation = " -> None"
            output_lines.append(f"def {py_name}({params_str}){ret_annotation}:")
            output_lines.append("    pass")
            output_lines.append("")

    return "\n".join(output_lines).rstrip() + "\n"


def generate_inline_class(type_name: str, prob_dir: Path) -> str:
    """Generate an inline class definition from Go struct."""
    go_stub = None
    for f in prob_dir.iterdir():
        if f.suffix == ".go" and f.name not in ("solution.go",) and "test" not in f.name:
            content = f.read_text()
            if f"type {type_name} struct" in content:
                go_stub = content
                break
    if not go_stub:
        return f"class {type_name}:\n    pass"

    if type_name == "Node":
        return (
            "class Node:\n"
            "    def __init__(self, val: int = 0, neighbors: list = None):\n"
            "        self.val = val\n"
            "        self.neighbors = neighbors if neighbors is not None else []"
        )
    elif type_name == "RandomNode":
        return (
            "class RandomNode:\n"
            "    def __init__(self, val: int = 0, next: 'RandomNode' = None, "
            "random: 'RandomNode' = None):\n"
            "        self.val = val\n"
            "        self.next = next\n"
            "        self.random = random"
        )
    else:
        return f"class {type_name}:\n    pass"


def generate_test_skeleton(prob_dir: Path, module_name: str) -> str:
    """Generate a Python test skeleton from Go tests."""
    go_test = None
    for f in sorted(prob_dir.iterdir()):
        if f.name.endswith("_test.go") and f.name != "helpers_test.go":
            go_test = f
            break
    if not go_test:
        return ""

    content = go_test.read_text()
    has_treenode = (prob_dir / "treenode.go").exists()
    has_listnode = (prob_dir / "listnode.go").exists()

    # Parse Go stub to get function names and detect class-based
    go_stub = prob_dir / f"{module_name}.go"
    stub_content = go_stub.read_text() if go_stub.exists() else ""
    is_class = bool(re.search(r'type\s+\w+\s+struct', stub_content)
                     and re.search(r'func\s+\(\w+\s+\*?\w+\)', stub_content))

    # Extract test function names and test data from Go
    test_funcs = re.findall(r'func\s+(Test\w+)\s*\(', content)

    # Try to extract test cases from table-driven tests
    test_cases = extract_go_test_cases(content)

    output_lines = ["import pytest"]

    # Determine imports
    if is_class:
        # Find the main class name
        class_names = re.findall(r'type\s+(\w+)\s+struct', stub_content)
        class_names = [c for c in class_names if c not in ("TreeNode", "ListNode")]
        if class_names:
            output_lines.append(f"from {module_name} import {class_names[0]}")
    else:
        # Find function names
        func_names = re.findall(r'func\s+(\w+)\s*\([^)]*\)', stub_content)
        func_names = [f for f in func_names if not f[0].isupper() or f in ("Constructor",)]
        # Filter out package-level funcs only
        real_funcs = []
        for fn in func_names:
            if not re.search(rf'func\s+\(\w+\s+\*?\w+\)\s+{fn}', stub_content):
                real_funcs.append(fn)
        if real_funcs:
            py_imports = [camel_to_snake(f) for f in real_funcs]
            output_lines.append(f"from {module_name} import {', '.join(py_imports)}")

    if has_treenode:
        output_lines.append("from tree_node import build_tree, tree_to_list")
    if has_listnode:
        output_lines.append("from list_node import build_list, list_to_array")

    output_lines.append("")
    output_lines.append("")

    if test_cases:
        for test_name, cases in test_cases.items():
            output_lines.append(f"# TODO: Translate test cases from Go")
            output_lines.append(f"# Go test: {test_name}")
            output_lines.append(f"# {len(cases)} test cases found")

            func_name = test_name.replace("Test", "")
            py_func_name = camel_to_snake(func_name)

            output_lines.append(f"@pytest.mark.parametrize(\"name\", [")
            for case in cases:
                case_name = case.get("name", "case")
                output_lines.append(f'    ("{case_name}"),')
            output_lines.append("])")
            output_lines.append(f"def test_{py_func_name}(name):")
            output_lines.append(f"    # TODO: implement test")
            output_lines.append(f"    pass")
            output_lines.append("")
    else:
        for tf in test_funcs:
            func_name = tf.replace("Test", "")
            py_func_name = camel_to_snake(func_name)
            output_lines.append(f"# TODO: Translate from Go test {tf}")
            output_lines.append(f"def test_{py_func_name}():")
            output_lines.append(f"    # TODO: implement test")
            output_lines.append(f"    pass")
            output_lines.append("")

    return "\n".join(output_lines).rstrip() + "\n"


def extract_go_test_cases(content: str) -> dict:
    """Extract test case names from Go table-driven tests."""
    result = {}
    # Find test functions
    test_blocks = re.finditer(
        r'func\s+(Test\w+)\s*\(t\s+\*testing\.T\)\s*\{(.*?)^}',
        content, re.DOTALL | re.MULTILINE
    )
    for m in test_blocks:
        test_name = m.group(1)
        body = m.group(2)
        # Extract case names
        case_names = re.findall(r'name:\s*"([^"]*)"', body)
        if case_names:
            result[test_name] = [{"name": n} for n in case_names]
    return result


def generate_solution_skeleton(prob_dir: Path, module_name: str) -> str:
    """Generate a Python solution skeleton from Go solution."""
    go_sol = prob_dir / "solution.go"
    if not go_sol.exists():
        return ""

    content = go_sol.read_text()
    has_treenode = (prob_dir / "treenode.go").exists()
    has_listnode = (prob_dir / "listnode.go").exists()

    # Detect class-based
    is_class = bool(re.search(r'type\s+Solve\w+\s+struct', content))

    output_lines = []
    typing_imports = set()

    # Parse all functions/methods
    for line in content.split("\n"):
        line_stripped = line.strip()
        func_info = parse_go_func(line_stripped)
        method_info = parse_go_method(line_stripped)
        info = func_info or method_info
        if info:
            for _, ptype in info["params"]:
                py_type = go_type_to_python(ptype)
                if "List[" in py_type:
                    typing_imports.add("List")
                if "Optional[" in py_type:
                    typing_imports.add("Optional")
            if info.get("return_type"):
                py_type = go_type_to_python(info["return_type"])
                if "List[" in py_type:
                    typing_imports.add("List")
                if "Optional[" in py_type:
                    typing_imports.add("Optional")

    if typing_imports:
        output_lines.append(f"from typing import {', '.join(sorted(typing_imports))}")
    if has_treenode:
        output_lines.append("from tree_node import TreeNode")
    if has_listnode:
        output_lines.append("from list_node import ListNode")
    if output_lines:
        output_lines.append("")
        output_lines.append("")

    if is_class:
        struct_names = re.findall(r'type\s+(Solve\w+)\s+struct', content)
        for sname in struct_names:
            output_lines.append(f"# TODO: Translate solution from Go")
            output_lines.append(f"class {sname}:")
            output_lines.append("    def __init__(self):")
            output_lines.append("        pass")
            output_lines.append("")
    else:
        for line in content.split("\n"):
            func_info = parse_go_func(line.strip())
            if func_info:
                py_name = camel_to_snake(func_info["name"])
                fparams = []
                for pname, ptype in func_info["params"]:
                    py_type = go_type_to_python(ptype)
                    py_pname = camel_to_snake(pname)
                    if py_pname in ("list", "type", "input", "next", "hash", "map", "set"):
                        py_pname += "_"
                    fparams.append(f"{py_pname}: {py_type}")
                params_str = ", ".join(fparams)
                ret = ""
                if func_info["return_type"]:
                    ret = f" -> {go_type_to_python(func_info['return_type'])}"
                output_lines.append(f"# TODO: Translate solution from Go")
                output_lines.append(f"def {py_name}({params_str}){ret}:")
                output_lines.append("    pass")
                output_lines.append("")

    return "\n".join(output_lines).rstrip() + "\n"


def process_problem(prob_dir: Path, dry_run: bool = False, skip_existing: bool = False) -> dict:
    """Process a single problem directory and generate Python files."""
    # Determine module name from Go stub
    go_stubs = [
        f for f in prob_dir.iterdir()
        if f.suffix == ".go"
        and f.name != "solution.go"
        and "_test" not in f.name
        and f.name not in ("treenode.go", "listnode.go", "helpers_test.go", "node.go",
                           "trienode.go")
    ]
    if not go_stubs:
        return {"skipped": True, "reason": "no Go stub found"}

    module_name = go_stubs[0].stem
    results = {"dir": str(prob_dir.relative_to(TEMPLATES_DIR)), "files": []}

    has_treenode = (prob_dir / "treenode.go").exists()
    has_listnode = (prob_dir / "listnode.go").exists()

    # 1. Generate stub
    stub_path = prob_dir / f"{module_name}.py"
    if not skip_existing or not stub_path.exists():
        stub_content = generate_stub(prob_dir, module_name)
        if stub_content:
            results["files"].append(str(stub_path.name))
            if not dry_run:
                stub_path.write_text(stub_content)

    # 2. Generate test skeleton
    test_path = prob_dir / f"test_{module_name}.py"
    if not skip_existing or not test_path.exists():
        test_content = generate_test_skeleton(prob_dir, module_name)
        if test_content:
            results["files"].append(str(test_path.name))
            if not dry_run:
                test_path.write_text(test_content)

    # 3. Generate solution skeleton
    sol_path = prob_dir / "solution.py"
    if not skip_existing or not sol_path.exists():
        sol_content = generate_solution_skeleton(prob_dir, module_name)
        if sol_content:
            results["files"].append("solution.py")
            if not dry_run:
                sol_path.write_text(sol_content)

    # 4. Generate helper files
    if has_treenode:
        helper_path = prob_dir / "tree_node.py"
        if not skip_existing or not helper_path.exists():
            results["files"].append("tree_node.py")
            if not dry_run:
                helper_path.write_text(TREE_NODE_PY)

    if has_listnode:
        helper_path = prob_dir / "list_node.py"
        if not skip_existing or not helper_path.exists():
            results["files"].append("list_node.py")
            if not dry_run:
                helper_path.write_text(LIST_NODE_PY)

    return results


def find_all_problems() -> list:
    """Find all problem directories under templates/problems/."""
    problems = []
    for category in sorted(TEMPLATES_DIR.iterdir()):
        if not category.is_dir():
            continue
        for problem in sorted(category.iterdir()):
            if not problem.is_dir():
                continue
            if problem.name == "assets":
                continue
            problems.append(problem)
    return problems


def main():
    parser = argparse.ArgumentParser(description="Generate Python files from Go templates")
    parser.add_argument("--all", action="store_true", help="Generate for all problems")
    parser.add_argument("--problem", type=str, help="Generate for a specific problem (e.g. 01_arrays_hashing/03_two_sum)")
    parser.add_argument("--skip-existing", action="store_true", help="Skip files that already exist")
    parser.add_argument("--dry-run", action="store_true", help="Show what would be created without writing")
    args = parser.parse_args()

    if not args.all and not args.problem:
        parser.print_help()
        sys.exit(1)

    if args.problem:
        prob_dir = TEMPLATES_DIR / args.problem
        if not prob_dir.exists():
            print(f"Error: {prob_dir} does not exist")
            sys.exit(1)
        problems = [prob_dir]
    else:
        problems = find_all_problems()

    total_files = 0
    for prob_dir in problems:
        result = process_problem(prob_dir, dry_run=args.dry_run, skip_existing=args.skip_existing)
        if result.get("skipped"):
            continue
        if result["files"]:
            prefix = "[DRY RUN] " if args.dry_run else ""
            print(f"{prefix}{result['dir']}: {', '.join(result['files'])}")
            total_files += len(result["files"])

    action = "Would create" if args.dry_run else "Created"
    print(f"\n{action} {total_files} files across {len(problems)} problems")


if __name__ == "__main__":
    main()

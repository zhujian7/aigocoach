#!/usr/bin/env python3
"""Fix empty Python test stubs by translating Go test data.

Usage:
    python scripts/fix_python_tests.py --all
    python scripts/fix_python_tests.py --problem 01_arrays_hashing/02_valid_anagram
    python scripts/fix_python_tests.py --all --dry-run
"""

import argparse
import re
import shutil
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
TEMPLATES_DIR = REPO_ROOT / "templates" / "problems"

SKIP_TESTS = {
    "01_arrays_hashing/01_contains_duplicate",
    "01_arrays_hashing/03_two_sum",
    "04_stack/02_min_stack",
    "06_linked_list/01_reverse_list",
    "07_trees/01_invert_tree",
}


def camel_to_snake(name: str) -> str:
    result = re.sub(r'([A-Z]+)([A-Z][a-z])', r'\1_\2', name)
    result = re.sub(r'([a-z0-9])([A-Z])', r'\1_\2', result)
    return result.lower()


# ── Go Value Parsing ──────────────────────────────────────────────


def split_at_top_level(text, delimiter=','):
    parts = []
    current = []
    depth = 0
    in_string = False
    in_char = False
    escape = False

    for ch in text:
        if escape:
            current.append(ch)
            escape = False
            continue
        if ch == '\\' and (in_string or in_char):
            current.append(ch)
            escape = True
            continue
        if ch == '"' and not in_char:
            in_string = not in_string
            current.append(ch)
            continue
        if ch == "'" and not in_string:
            in_char = not in_char
            current.append(ch)
            continue
        if in_string or in_char:
            current.append(ch)
            continue
        if ch in '{([':
            depth += 1
            current.append(ch)
        elif ch in '})]':
            depth -= 1
            current.append(ch)
        elif ch == delimiter and depth == 0:
            parts.append(''.join(current))
            current = []
        else:
            current.append(ch)

    if current:
        parts.append(''.join(current))
    return parts


def parse_go_value(text):
    text = text.strip()

    if text == 'nil':
        return 'None'
    if text == 'true':
        return 'True'
    if text == 'false':
        return 'False'
    if text.startswith('"') and text.endswith('"'):
        return text
    if re.match(r"^'(.)'$", text):
        return f'"{text[1]}"'
    if re.match(r'^-?\d+$', text):
        return text
    if re.match(r'^-?\d+\.\d+$', text):
        return text
    if text == 'math.MaxInt32':
        return '2147483647'
    if text == 'math.MinInt32':
        return '-2147483648'
    if text == 'math.MaxInt64':
        return '9223372036854775807'

    m = re.match(r'\[\]byte\("([^"]*)"\)', text)
    if m:
        return f'"{m.group(1)}"'

    m = re.match(r"\[\]byte\{(.*)\}$", text, re.DOTALL)
    if m:
        chars = re.findall(r"'(.)'", m.group(1))
        if chars:
            return '[' + ', '.join(f'"{c}"' for c in chars) + ']'
        inner = m.group(1).strip()
        if not inner:
            return '[]'
        elems = split_at_top_level(inner)
        return '[' + ', '.join(parse_go_value(e.strip()) for e in elems if e.strip()) + ']'

    m = re.match(r'\[\]\[\]byte\{(.*)\}$', text, re.DOTALL)
    if m:
        inner = m.group(1).strip()
        if not inner:
            return '[]'
        rows = split_at_top_level(inner)
        py_rows = []
        for row in rows:
            row = row.strip()
            if not row:
                continue
            rm = re.match(r'(?:\[\]byte)?\{(.*)\}$', row, re.DOTALL)
            if rm:
                chars = re.findall(r"'(.)'", rm.group(1))
                if chars:
                    py_rows.append('[' + ', '.join(f'"{c}"' for c in chars) + ']')
                else:
                    py_rows.append('[]')
            else:
                py_rows.append(parse_go_value(row))
        return '[' + ', '.join(py_rows) + ']'

    m = re.match(r'\[\](\[\]\w+)\{(.*)\}$', text, re.DOTALL)
    if m:
        inner = m.group(2).strip()
        if not inner:
            return '[]'
        elements = split_at_top_level(inner)
        py_elements = []
        for elem in elements:
            elem = elem.strip()
            if not elem:
                continue
            if elem == 'nil':
                py_elements.append('None')
                continue
            im = re.match(r'(?:\[\]\w+)?\{(.*)\}$', elem, re.DOTALL)
            if im:
                inner_vals = im.group(1).strip()
                if not inner_vals:
                    py_elements.append('[]')
                else:
                    sub = split_at_top_level(inner_vals)
                    py_elements.append('[' + ', '.join(
                        parse_go_value(s.strip()) for s in sub if s.strip()
                    ) + ']')
            else:
                py_elements.append(parse_go_value(elem))
        return '[' + ', '.join(py_elements) + ']'

    m = re.match(r'\[\]\w+\{(.*)\}$', text, re.DOTALL)
    if m:
        inner = m.group(1).strip()
        if not inner:
            return '[]'
        elements = split_at_top_level(inner)
        return '[' + ', '.join(
            parse_go_value(e.strip()) for e in elements if e.strip()
        ) + ']'

    return text


# ── Go Test File Parsing ──────────────────────────────────────────


def parse_struct_fields(fields_str):
    fields = []
    for line in fields_str.strip().split('\n'):
        line = line.strip()
        if not line or line.startswith('//'):
            continue
        if '//' in line:
            line = line[:line.index('//')].strip()
        if not line:
            continue
        if '[]struct{' in line or 'struct{' in line or 'struct {' in line:
            return None
        tokens = line.split()
        if len(tokens) < 2:
            continue
        go_type = tokens[-1]
        names_part = ' '.join(tokens[:-1])
        for name in re.split(r'[,\s]+', names_part):
            name = name.strip()
            if name:
                fields.append((name, go_type))
    return fields


def find_matching_brace(text, start):
    depth = 0
    in_string = False
    in_char = False
    escape = False
    for i in range(start, len(text)):
        ch = text[i]
        if escape:
            escape = False
            continue
        if ch == '\\' and (in_string or in_char):
            escape = True
            continue
        if ch == '"' and not in_char:
            in_string = not in_string
            continue
        if ch == "'" and not in_string:
            in_char = not in_char
            continue
        if in_string or in_char:
            continue
        if ch == '{':
            depth += 1
        elif ch == '}':
            depth -= 1
            if depth == 0:
                return i
    return -1


def extract_test_functions(go_content):
    results = {}
    pattern = re.compile(r'func\s+(Test\w+)\s*\(t\s+\*testing\.T\)\s*\{')
    for m in pattern.finditer(go_content):
        func_name = m.group(1)
        func_brace_start = m.end() - 1
        func_end = find_matching_brace(go_content, func_brace_start)
        if func_end < 0:
            continue
        func_body = go_content[func_brace_start:func_end + 1]
        results[func_name] = func_body
    return results


def extract_test_data(func_body):
    struct_match = re.search(
        r'tests\s*:=\s*\[\]struct\s*\{',
        func_body
    )
    if not struct_match:
        return None

    struct_brace_start = struct_match.end() - 1
    struct_brace_end = find_matching_brace(func_body, struct_brace_start)
    if struct_brace_end < 0:
        return None

    fields_str = func_body[struct_brace_start + 1:struct_brace_end]
    fields = parse_struct_fields(fields_str)
    if not fields:
        return None

    data_brace_start = func_body.index('{', struct_brace_end + 1)
    data_brace_end = find_matching_brace(func_body, data_brace_start)
    if data_brace_end < 0:
        return None

    data_inner = func_body[data_brace_start + 1:data_brace_end]
    raw_cases = split_at_top_level(data_inner)

    cases = []
    field_names = [f[0] for f in fields]
    for raw in raw_cases:
        raw = raw.strip()
        if not raw:
            continue
        if raw.startswith('{'):
            inner = raw[1:]
            if inner.endswith('}'):
                inner = inner[:-1]
            inner = inner.strip()
        else:
            continue

        parts = split_at_top_level(inner)
        case = {}

        first = parts[0].strip() if parts else ''
        colon_pos = first.find(':')
        is_named = (colon_pos > 0 and first[:colon_pos].strip() in field_names)

        if is_named:
            for part in parts:
                part = part.strip()
                if not part:
                    continue
                cp = part.find(':')
                if cp > 0:
                    fname = part[:cp].strip()
                    fval = part[cp + 1:].strip()
                    case[fname] = fval
        else:
            for i, part in enumerate(parts):
                part = part.strip()
                if not part:
                    continue
                if i < len(field_names):
                    case[field_names[i]] = part

        if case:
            cases.append(case)

    for_match = re.search(
        r'for\s+_,\s+tt\s*:=\s*range\s+tests\s*\{',
        func_body
    )
    assertion_body = ''
    if for_match:
        for_brace = for_match.end() - 1
        for_end = find_matching_brace(func_body, for_brace)
        if for_end > 0:
            assertion_body = func_body[for_brace + 1:for_end]

    return {
        'fields': fields,
        'cases': cases,
        'assertion_body': assertion_body,
    }


# ── Pattern Detection ─────────────────────────────────────────────


def detect_test_type(test_data, prob_dir):
    body = test_data['assertion_body']
    fields = test_data['fields']
    field_names = {f[0] for f in fields}

    has_tree_build = 'buildTreeHelper' in body or 'buildTree(' in body
    has_list_build = 'buildList(' in body
    has_operations = 'operations' in field_names or 'ops' in field_names
    has_cycle_pos = 'cyclePos' in field_names
    has_sort = bool(re.search(r'sort[\.\w]*\(', body))
    has_got_assign = bool(re.search(r'got\s*:=', body))
    has_random_list = 'randomIndices' in field_names or 'buildRandomList' in body

    if has_operations:
        return 'class'
    if has_cycle_pos:
        return 'cycle'
    if has_random_list:
        return 'random_list'
    if has_tree_build and has_got_assign:
        tree_return = ('treeToSlice' in body or 'treeToList' in body)
        list_return = ('listToSlice' in body or 'listToArray' in body)
        if tree_return:
            return 'tree_return_tree'
        if list_return:
            return 'tree_return_list'
        return 'tree'
    if has_list_build and has_got_assign:
        list_return = ('listToSlice' in body or 'listToArray' in body)
        if list_return:
            return 'list_return_list'
        return 'list'
    if has_list_build and not has_got_assign:
        return 'list_mutation'
    if not has_got_assign and not has_operations:
        return 'mutation'
    if has_sort:
        return 'sorted'
    return 'simple'


WRAPPER_FUNCS = {
    'listToSlice', 'listToArray', 'treeToSlice', 'treeToList',
}
HELPER_FUNCS = {
    'buildTreeHelper', 'buildTree', 'buildList', 'buildGraph',
    'buildRandomList', 'sort', 'reflect', 'fmt',
} | WRAPPER_FUNCS


def find_tested_func(body):
    m = re.search(
        r'got\s*:=\s*(?:listToSlice|treeToSlice|listToArray|treeToList)\(\s*(\w+)\(',
        body
    )
    if m:
        return m.group(1)
    m = re.search(r'got\s*:=\s*(\w+)\(', body)
    if m and m.group(1) not in HELPER_FUNCS:
        return m.group(1)
    m = re.search(r'^\s+(\w+)\(tt\.', body, re.MULTILINE)
    if m and m.group(1) not in HELPER_FUNCS:
        return m.group(1)
    m = re.search(r'^\s+(\w+)\(\w+\)', body, re.MULTILINE)
    if m and m.group(1) not in HELPER_FUNCS:
        return m.group(1)
    return None


def find_func_args(body, fields):
    m = re.search(r'(?:got|result)\s*:=\s*\w+\(([^)]+)\)', body)
    if not m:
        m = re.search(r'^\s+\w+\(([^)]+)\)', body, re.MULTILINE)
    if not m:
        return []

    args_str = m.group(1)
    args = []
    for arg in args_str.split(','):
        arg = arg.strip()
        am = re.match(r'tt\.(\w+)', arg)
        if am:
            args.append(am.group(1))
    return args


def find_expect_field(fields):
    field_names = [f[0] for f in fields]
    for name in ('want', 'expected', 'result', 'ans', 'output'):
        if name in field_names:
            return name
    for name in field_names:
        if name != 'name':
            pass
    return field_names[-1] if field_names else 'want'


# ── Python Test Generation ────────────────────────────────────────


def go_type_to_annotation(go_type):
    mapping = {
        'int': 'int', 'int32': 'int', 'int64': 'int',
        'float64': 'float', 'float32': 'float',
        'string': 'str', 'bool': 'bool', 'byte': 'str',
    }
    return mapping.get(go_type, go_type)


def format_py_value(val_str, go_type=''):
    return parse_go_value(val_str)


def build_parametrize_data(cases, param_names, fields_map):
    lines = []
    for case in cases:
        vals = []
        for pname in param_names:
            raw = case.get(pname, 'None')
            go_type = fields_map.get(pname, '')
            vals.append(format_py_value(raw, go_type))
        lines.append('    (' + ', '.join(vals) + '),')
    return '\n'.join(lines)


def generate_simple_test(test_data, module_name, py_func_name, prob_dir):
    fields = test_data['fields']
    cases = test_data['cases']
    body = test_data['assertion_body']

    fields_map = {f[0]: f[1] for f in fields}
    expect_field = find_expect_field(fields)

    func_args_fields = find_func_args(body, fields)
    if not func_args_fields:
        non_meta = [f[0] for f in fields if f[0] not in ('name', expect_field)]
        func_args_fields = non_meta

    param_names = ['name'] + func_args_fields + [expect_field]
    param_names = [p for p in param_names if p in fields_map or p == 'name']

    if 'name' not in fields_map:
        param_names = [p for p in param_names if p != 'name']

    data = build_parametrize_data(cases, param_names, fields_map)
    params_str = ', '.join(param_names)
    args_str = ', '.join(func_args_fields)

    lines = ['import pytest']
    lines.append(f'from {module_name} import {py_func_name}')
    lines.append('')
    lines.append('')
    lines.append(f'@pytest.mark.parametrize("{params_str}", [')
    lines.append(data)
    lines.append('])')

    func_params = params_str
    lines.append(f'def test_{py_func_name}({func_params}):')
    name_ref = 'name' if 'name' in param_names else 'f"case"'
    lines.append(f'    result = {py_func_name}({args_str})')

    expect_type = fields_map.get(expect_field, '')
    if expect_type in ('[]int', '[]string', '[]float64', '[]int32'):
        if 'name' in param_names:
            lines.append(
                f'    assert result == {expect_field}, '
                f'f"{{{name_ref}}}: got {{result}}, want {{{expect_field}}}"'
            )
        else:
            lines.append(f'    assert result == {expect_field}')
    else:
        if 'name' in param_names:
            lines.append(
                f'    assert result == {expect_field}, '
                f'f"{{{name_ref}}}: got {{result}}, want {{{expect_field}}}"'
            )
        else:
            lines.append(f'    assert result == {expect_field}')

    return '\n'.join(lines) + '\n'


def generate_sorted_test(test_data, module_name, py_func_name, prob_dir):
    fields = test_data['fields']
    cases = test_data['cases']
    body = test_data['assertion_body']

    fields_map = {f[0]: f[1] for f in fields}
    expect_field = find_expect_field(fields)

    func_args_fields = find_func_args(body, fields)
    if not func_args_fields:
        non_meta = [f[0] for f in fields if f[0] not in ('name', expect_field)]
        func_args_fields = non_meta

    param_names = ['name'] + func_args_fields + [expect_field]
    param_names = [p for p in param_names if p in fields_map or p == 'name']
    if 'name' not in fields_map:
        param_names = [p for p in param_names if p != 'name']

    data = build_parametrize_data(cases, param_names, fields_map)
    params_str = ', '.join(param_names)
    args_str = ', '.join(func_args_fields)

    expect_type = fields_map.get(expect_field, '')
    is_2d = expect_type.startswith('[][]')

    lines = ['import pytest']
    lines.append(f'from {module_name} import {py_func_name}')
    lines.append('')
    lines.append('')

    if is_2d:
        lines.append('')
        lines.append('def sort_2d(lst):')
        lines.append('    if lst is None:')
        lines.append('        return None')
        lines.append('    return sorted([sorted(sub) for sub in lst])')
        lines.append('')
        lines.append('')

    lines.append(f'@pytest.mark.parametrize("{params_str}", [')
    lines.append(data)
    lines.append('])')
    lines.append(f'def test_{py_func_name}({params_str}):')
    lines.append(f'    result = {py_func_name}({args_str})')

    if is_2d:
        lines.append(
            f'    assert sort_2d(result) == sort_2d({expect_field}), '
            f'f"{{name}}: got {{result}}, want {{{expect_field}}}"'
        )
    else:
        lines.append(
            f'    assert sorted(result) == sorted({expect_field}), '
            f'f"{{name}}: got {{result}}, want {{{expect_field}}}"'
        )

    return '\n'.join(lines) + '\n'


def generate_tree_test(test_data, module_name, py_func_name, prob_dir, return_type):
    fields = test_data['fields']
    cases = test_data['cases']
    body = test_data['assertion_body']

    fields_map = {f[0]: f[1] for f in fields}
    expect_field = find_expect_field(fields)

    tree_build_matches = re.findall(r'(\w+)\s*:=\s*buildTreeHelper\(tt\.(\w+)\)', body)
    tree_vars = {var: field for var, field in tree_build_matches}

    vals_field = None
    if tree_vars:
        vals_field = list(tree_vars.values())[0]
    if not vals_field:
        for f in fields:
            if f[0] in ('vals', 'root', 'nodes', 'values', 'tree'):
                vals_field = f[0]
                break
    if not vals_field:
        for f in fields:
            if f[1] == '[]int' and f[0] not in ('name', expect_field):
                vals_field = f[0]
                break

    other_args = []
    for f in fields:
        if f[0] not in ('name', vals_field, expect_field):
            if f[0] not in tree_vars.values():
                other_args.append(f[0])

    second_tree_field = None
    if len(tree_vars) > 1:
        for field in tree_vars.values():
            if field != vals_field:
                second_tree_field = field
                break

    param_names = ['name']
    if vals_field:
        param_names.append(vals_field)
    if second_tree_field:
        param_names.append(second_tree_field)
    param_names.extend(other_args)
    param_names.append(expect_field)
    if 'name' not in fields_map:
        param_names = [p for p in param_names if p != 'name']

    data = build_parametrize_data(cases, param_names, fields_map)
    params_str = ', '.join(param_names)

    lines = ['import pytest']
    if return_type in ('tree_return_tree',):
        lines.append('from tree_node import build_tree, tree_to_list')
    else:
        lines.append('from tree_node import build_tree')
    lines.append(f'from {module_name} import {py_func_name}')
    lines.append('')
    lines.append('')
    lines.append(f'@pytest.mark.parametrize("{params_str}", [')
    lines.append(data)
    lines.append('])')
    lines.append(f'def test_{py_func_name}({params_str}):')

    root_var = vals_field or 'vals'
    lines.append(f'    root = build_tree({root_var})')

    call_args_parts = ['root']
    if second_tree_field:
        lines.append(f'    root2 = build_tree({second_tree_field})')
        call_args_parts.append('root2')
    for arg in other_args:
        call_args_parts.append(arg)
    call_args = ', '.join(call_args_parts)

    if return_type == 'tree_return_tree':
        lines.append(f'    got = tree_to_list({py_func_name}({call_args}))')
    else:
        lines.append(f'    got = {py_func_name}({call_args})')

    has_sort = bool(re.search(r'sort[\.\w]*\(', body))
    if has_sort:
        lines.append(
            f'    assert sorted(got or []) == sorted({expect_field} or []), '
            f'f"{{name}}: got {{got}}, want {{{expect_field}}}"'
        )
    else:
        lines.append(
            f'    assert got == {expect_field}, '
            f'f"{{name}}: got {{got}}, want {{{expect_field}}}"'
        )

    return '\n'.join(lines) + '\n'


def generate_list_test(test_data, module_name, py_func_name, prob_dir, return_type):
    fields = test_data['fields']
    cases = test_data['cases']
    body = test_data['assertion_body']

    fields_map = {f[0]: f[1] for f in fields}
    expect_field = find_expect_field(fields)

    build_calls = re.findall(r'(\w+)\s*:=\s*buildList\(tt\.(\w+)\)', body)
    list_vars = {var: field for var, field in build_calls}

    func_call_match = re.search(
        rf'{py_func_name}|{camel_to_snake(py_func_name)}|'
        + r'(\w+)\(',
        body
    )
    go_func = find_tested_func(body) or py_func_name
    func_call_re = re.search(rf'{re.escape(go_func)}\(([^)]+)\)', body)

    ordered_list_fields = []
    non_list_args = []
    if func_call_re:
        for arg in func_call_re.group(1).split(','):
            arg = arg.strip()
            if arg in list_vars:
                ordered_list_fields.append(list_vars[arg])
            elif arg.startswith('tt.'):
                non_list_args.append(arg[3:])

    if not ordered_list_fields:
        for f in fields:
            if f[0] in ('vals', 'head', 'list', 'list1', 'nodes', 'values'):
                ordered_list_fields.append(f[0])
                break
        if not ordered_list_fields:
            for f in fields:
                if f[1] == '[]int' and f[0] not in ('name', expect_field):
                    ordered_list_fields.append(f[0])
                    break

    non_list_args = [a for a in non_list_args
                     if a not in ordered_list_fields and a != expect_field and a != 'name']

    param_names = ['name'] + ordered_list_fields + non_list_args + [expect_field]
    param_names = [p for p in param_names if p in fields_map or p == 'name']
    if 'name' not in fields_map:
        param_names = [p for p in param_names if p != 'name']

    data = build_parametrize_data(cases, param_names, fields_map)
    params_str = ', '.join(param_names)

    lines = ['import pytest']
    lines.append('from list_node import build_list, list_to_array')
    lines.append(f'from {module_name} import {py_func_name}')
    lines.append('')
    lines.append('')
    lines.append(f'@pytest.mark.parametrize("{params_str}", [')
    lines.append(data)
    lines.append('])')
    lines.append(f'def test_{py_func_name}({params_str}):')

    list_var_names = []
    for i, field in enumerate(ordered_list_fields):
        var = f'l{i + 1}' if len(ordered_list_fields) > 1 else 'head'
        lines.append(f'    {var} = build_list({field})')
        list_var_names.append(var)

    call_args_list = list_var_names + non_list_args
    call_args = ', '.join(call_args_list)

    if return_type == 'list_return_list':
        lines.append(f'    got = list_to_array({py_func_name}({call_args}))')
    elif return_type == 'list_mutation':
        lines.append(f'    {py_func_name}({call_args})')
        head_var = list_var_names[0] if list_var_names else 'head'
        lines.append(f'    got = list_to_array({head_var})')
    else:
        lines.append(f'    got = {py_func_name}({call_args})')

    lines.append(
        f'    assert got == {expect_field}, '
        f'f"{{name}}: got {{got}}, want {{{expect_field}}}"'
    )

    return '\n'.join(lines) + '\n'


def generate_mutation_test(test_data, module_name, py_func_name, prob_dir):
    fields = test_data['fields']
    cases = test_data['cases']
    body = test_data['assertion_body']

    fields_map = {f[0]: f[1] for f in fields}
    expect_field = find_expect_field(fields)

    input_fields = [f[0] for f in fields if f[0] not in ('name', expect_field)]

    param_names = ['name'] + input_fields + [expect_field]
    if 'name' not in fields_map:
        param_names = [p for p in param_names if p != 'name']

    data = build_parametrize_data(cases, param_names, fields_map)
    params_str = ', '.join(param_names)
    args_str = ', '.join(input_fields)
    mutated_field = input_fields[0] if input_fields else 'data'

    lines = ['import pytest']
    lines.append(f'from {module_name} import {py_func_name}')
    lines.append('')
    lines.append('')
    lines.append(f'@pytest.mark.parametrize("{params_str}", [')
    lines.append(data)
    lines.append('])')
    lines.append(f'def test_{py_func_name}({params_str}):')
    lines.append(f'    {py_func_name}({args_str})')
    lines.append(
        f'    assert {mutated_field} == {expect_field}, '
        f'f"{{name}}: got {{{mutated_field}}}, want {{{expect_field}}}"'
    )

    return '\n'.join(lines) + '\n'


def generate_cycle_test(test_data, module_name, py_func_name, prob_dir):
    fields = test_data['fields']
    cases = test_data['cases']
    fields_map = {f[0]: f[1] for f in fields}
    expect_field = find_expect_field(fields)

    vals_field = 'vals'
    for f in fields:
        if f[0] in ('vals', 'values', 'nums'):
            vals_field = f[0]
            break

    param_names = ['name', vals_field, 'cyclePos', expect_field]
    if 'name' not in fields_map:
        param_names = [p for p in param_names if p != 'name']

    data = build_parametrize_data(cases, param_names, fields_map)
    params_str = ', '.join(param_names)

    lines = ['import pytest']
    lines.append('from list_node import build_list, ListNode')
    lines.append(f'from {module_name} import {py_func_name}')
    lines.append('')
    lines.append('')
    lines.append(f'def build_list_with_cycle({vals_field}, cycle_pos):')
    lines.append(f'    head = build_list({vals_field})')
    lines.append(f'    if cycle_pos < 0 or head is None:')
    lines.append(f'        return head')
    lines.append(f'    tail = head')
    lines.append(f'    while tail.next:')
    lines.append(f'        tail = tail.next')
    lines.append(f'    target = head')
    lines.append(f'    for _ in range(cycle_pos):')
    lines.append(f'        target = target.next')
    lines.append(f'    tail.next = target')
    lines.append(f'    return head')
    lines.append('')
    lines.append('')
    lines.append(f'@pytest.mark.parametrize("{params_str}", [')
    lines.append(data)
    lines.append('])')
    lines.append(f'def test_{py_func_name}({params_str}):')
    lines.append(f'    head = build_list_with_cycle({vals_field}, cyclePos)')
    lines.append(
        f'    assert {py_func_name}(head) == {expect_field}, '
        f'f"{{name}}"'
    )

    return '\n'.join(lines) + '\n'


def generate_class_test(test_data, module_name, go_func_name, prob_dir):
    fields = test_data['fields']
    cases = test_data['cases']
    body = test_data['assertion_body']
    fields_map = {f[0]: f[1] for f in fields}

    go_stub = prob_dir / f"{module_name}.go"
    stub_content = go_stub.read_text() if go_stub.exists() else ""

    class_names = re.findall(r'type\s+(\w+)\s+struct', stub_content)
    class_names = [c for c in class_names if c not in ('TreeNode', 'ListNode', 'TrieNode')]
    class_name = class_names[0] if class_names else module_name.title().replace('_', '')

    ops_field = 'operations'
    if 'ops' in fields_map:
        ops_field = 'ops'

    expect_field = find_expect_field(fields)

    value_fields = [f[0] for f in fields
                    if f[0] not in ('name', ops_field, expect_field)]

    param_names = ['name', ops_field] + value_fields + [expect_field]
    if 'name' not in fields_map:
        param_names = [p for p in param_names if p != 'name']

    data = build_parametrize_data(cases, param_names, fields_map)
    params_str = ', '.join(param_names)

    switch_cases = re.findall(r'case\s+"(\w+)":', body)

    constructor_match = re.search(
        r'(?:New|Constructor)\w*\(([^)]*)\)', body
    )
    constructor_args = ''
    if constructor_match:
        raw_args = constructor_match.group(1).strip()
        if raw_args:
            arg_refs = re.findall(r'tt\.(\w+)', raw_args)
            idx_refs = re.findall(r'tt\.(\w+)\[0\]', raw_args)
            if idx_refs:
                constructor_args = ', '.join(f'{a}[0]' for a in idx_refs)
            elif arg_refs:
                constructor_args = ', '.join(arg_refs)

    py_class = class_name
    py_var = 'obj'

    lines = ['import pytest']
    lines.append(f'from {module_name} import {py_class}')
    lines.append('')
    lines.append('')
    lines.append(f'@pytest.mark.parametrize("{params_str}", [')
    lines.append(data)
    lines.append('])')
    lines.append(f'def test_{camel_to_snake(class_name)}({params_str}):')
    lines.append(f'    {py_var} = {py_class}({constructor_args})')
    lines.append(f'    for i, op in enumerate({ops_field}):')

    for j, op_name in enumerate(switch_cases):
        py_method = camel_to_snake(op_name)
        prefix = 'if' if j == 0 else 'elif'

        has_assert = bool(re.search(
            rf'case\s+"{op_name}".*?(?:got|result)\s*:=.*?{op_name}\(',
            body, re.DOTALL
        ))
        has_arg = bool(re.search(
            rf'{op_name}\(tt\.\w+\[i\]', body
        ))

        if has_arg and has_assert:
            val_ref = f'{value_fields[0]}[i]' if value_fields else 'None'
            lines.append(f'        {prefix} op == "{op_name}":')
            lines.append(
                f'            assert {py_var}.{py_method}({val_ref}) == {expect_field}[i], '
                f'f"{{name}} step {{i}}: {op_name}"'
            )
        elif has_assert:
            lines.append(f'        {prefix} op == "{op_name}":')
            lines.append(
                f'            assert {py_var}.{py_method}() == {expect_field}[i], '
                f'f"{{name}} step {{i}}: {op_name}"'
            )
        elif has_arg:
            val_ref = f'{value_fields[0]}[i]' if value_fields else 'None'
            lines.append(f'        {prefix} op == "{op_name}":')
            lines.append(f'            {py_var}.{py_method}({val_ref})')
        else:
            lines.append(f'        {prefix} op == "{op_name}":')
            lines.append(f'            {py_var}.{py_method}()')

    return '\n'.join(lines) + '\n'


def generate_python_test(prob_dir, module_name):
    go_test = None
    for f in sorted(prob_dir.iterdir()):
        if f.name.endswith('_test.go') and f.name != 'helpers_test.go':
            go_test = f
            break
    if not go_test:
        return None

    go_content = go_test.read_text()
    test_funcs = extract_test_functions(go_content)

    if not test_funcs:
        return None

    first_func_name = list(test_funcs.keys())[0]
    func_body = test_funcs[first_func_name]
    test_data = extract_test_data(func_body)

    if not test_data or not test_data['cases']:
        return None

    go_func = find_tested_func(test_data['assertion_body'])
    if go_func:
        py_func_name = camel_to_snake(go_func)
    else:
        py_func_name = camel_to_snake(first_func_name.replace('Test', ''))

    test_type = detect_test_type(test_data, prob_dir)

    generators = {
        'simple': generate_simple_test,
        'sorted': generate_sorted_test,
        'mutation': generate_mutation_test,
        'cycle': generate_cycle_test,
    }

    if test_type == 'class':
        return generate_class_test(test_data, module_name, first_func_name, prob_dir)
    elif test_type in ('tree', 'tree_return_tree', 'tree_return_list'):
        return generate_tree_test(test_data, module_name, py_func_name, prob_dir, test_type)
    elif test_type in ('list', 'list_return_list', 'list_mutation'):
        return generate_list_test(test_data, module_name, py_func_name, prob_dir, test_type)
    elif test_type in generators:
        return generators[test_type](test_data, module_name, py_func_name, prob_dir)
    else:
        return generate_simple_test(test_data, module_name, py_func_name, prob_dir)


# ── Main ──────────────────────────────────────────────────────────


def find_all_problems():
    problems = []
    for category in sorted(TEMPLATES_DIR.iterdir()):
        if not category.is_dir():
            continue
        for problem in sorted(category.iterdir()):
            if not problem.is_dir() or problem.name == 'assets':
                continue
            problems.append(problem)
    return problems


def get_module_name(prob_dir):
    go_stubs = [
        f for f in prob_dir.iterdir()
        if f.suffix == '.go'
        and f.name != 'solution.go'
        and '_test' not in f.name
        and f.name not in ('treenode.go', 'listnode.go', 'helpers_test.go',
                           'node.go', 'trienode.go')
    ]
    return go_stubs[0].stem if go_stubs else None


def is_broken_test(prob_dir, module_name):
    test_file = prob_dir / f'test_{module_name}.py'
    if not test_file.exists():
        return True
    content = test_file.read_text()
    return '# TODO: implement test' in content or ('pass' in content and 'assert' not in content)


def main():
    parser = argparse.ArgumentParser(description='Fix empty Python test stubs')
    parser.add_argument('--all', action='store_true', help='Fix all broken tests')
    parser.add_argument('--problem', type=str, help='Fix a specific problem')
    parser.add_argument('--dry-run', action='store_true', help='Preview without writing')
    parser.add_argument('--force', action='store_true', help='Overwrite even non-broken tests')
    args = parser.parse_args()

    if not args.all and not args.problem:
        parser.print_help()
        sys.exit(1)

    if args.problem:
        problems = [TEMPLATES_DIR / args.problem]
    else:
        problems = find_all_problems()

    fixed = 0
    skipped = 0
    failed = 0
    failures = []

    for prob_dir in problems:
        rel = prob_dir.relative_to(TEMPLATES_DIR)
        rel_str = str(rel)

        if rel_str in SKIP_TESTS and not args.force:
            skipped += 1
            continue

        module_name = get_module_name(prob_dir)
        if not module_name:
            continue

        if not args.force and not is_broken_test(prob_dir, module_name):
            skipped += 1
            continue

        try:
            result = generate_python_test(prob_dir, module_name)
        except Exception as e:
            failed += 1
            failures.append((rel_str, str(e)))
            continue

        if not result:
            failed += 1
            failures.append((rel_str, 'could not parse Go test'))
            continue

        test_path = prob_dir / f'test_{module_name}.py'
        prefix = '[DRY RUN] ' if args.dry_run else ''
        print(f'{prefix}Fixed: {rel_str}/test_{module_name}.py')

        if not args.dry_run:
            test_path.write_text(result)

            progress_dir = REPO_ROOT / 'my-progress' / 'round-1' / 'problems' / rel
            if progress_dir.exists():
                progress_test = progress_dir / f'test_{module_name}.py'
                shutil.copy2(test_path, progress_test)

        fixed += 1

    print(f'\nResults: {fixed} fixed, {skipped} skipped, {failed} failed')
    if failures:
        print('\nFailed:')
        for path, reason in failures:
            print(f'  {path}: {reason}')


if __name__ == '__main__':
    main()

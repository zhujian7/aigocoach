import pytest
from clone_graph import Node, clone_graph


def build_graph(adj_list):
    """Build a graph from an adjacency list (1-indexed) and return node with val=1."""
    if not adj_list:
        return None
    nodes = [None] + [Node(i + 1) for i in range(len(adj_list))]
    for i, neighbors in enumerate(adj_list):
        for n in neighbors:
            nodes[i + 1].neighbors.append(nodes[n])
    return nodes[1]


def collect_nodes(node):
    """BFS to collect all nodes as {val: node}."""
    if node is None:
        return {}
    visited = {}
    queue = [node]
    visited[node.val] = node
    while queue:
        cur = queue.pop(0)
        for n in cur.neighbors:
            if n.val not in visited:
                visited[n.val] = n
                queue.append(n)
    return visited


def graph_to_adj(node):
    """Convert graph to sorted adjacency list for comparison."""
    nodes = collect_nodes(node)
    if not nodes:
        return []
    result = []
    for v in sorted(nodes.keys()):
        result.append(sorted(n.val for n in nodes[v].neighbors))
    return result


@pytest.mark.parametrize("name, adjList", [
    ("four node cycle", [[2, 4], [1, 3], [2, 4], [1, 3]]),
    ("single node no neighbors", [[]]),
    ("nil graph", []),
    ("two connected nodes", [[2], [1]]),
    ("three node chain", [[2], [1, 3], [2]]),
    ("star graph", [[2, 3, 4], [1], [1], [1]]),
])
def test_clone_graph(name, adjList):
    original = build_graph(adjList)
    cloned = clone_graph(original)

    if original is None:
        assert cloned is None, f"{name}: expected None, got non-None"
        return

    orig_nodes = collect_nodes(original)
    clone_nodes = collect_nodes(cloned)

    assert len(orig_nodes) == len(clone_nodes), (
        f"{name}: node count mismatch: original={len(orig_nodes)}, "
        f"cloned={len(clone_nodes)}"
    )

    for val, o_node in orig_nodes.items():
        assert val in clone_nodes, f"{name}: cloned graph missing node {val}"
        c_node = clone_nodes[val]
        assert o_node is not c_node, (
            f"{name}: node {val} is same pointer in original and clone"
        )
        assert len(o_node.neighbors) == len(c_node.neighbors), (
            f"{name}: node {val} neighbor count mismatch"
        )

    got_adj = graph_to_adj(cloned)
    want_adj = graph_to_adj(original)
    assert got_adj == want_adj, f"{name}: adjacency mismatch: got {got_adj}, want {want_adj}"

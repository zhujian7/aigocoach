import pytest
from copy_random_list import RandomNode, copy_random_list


def build_random_list(vals, random_indices):
    """Build a RandomNode list from vals and random_indices.
    random_indices[i] is the index that node i's random points to,
    or -1 for None.
    """
    if not vals:
        return None
    nodes = [RandomNode(v) for v in vals]
    for i in range(len(nodes) - 1):
        nodes[i].next = nodes[i + 1]
    for i, ri in enumerate(random_indices):
        if ri >= 0:
            nodes[i].random = nodes[ri]
    return nodes[0]


def random_list_to_arrays(head):
    """Convert a RandomNode list to (vals, random_indices) tuple."""
    index_map = {}
    idx = 0
    cur = head
    while cur:
        index_map[id(cur)] = idx
        idx += 1
        cur = cur.next
    vals = []
    randoms = []
    cur = head
    while cur:
        vals.append(cur.val)
        if cur.random is not None:
            randoms.append(index_map[id(cur.random)])
        else:
            randoms.append(-1)
        cur = cur.next
    return vals, randoms


@pytest.mark.parametrize("name,vals,random_indices", [
    ("nil list", None, None),
    ("single no random", [1], [-1]),
    ("single self random", [1], [0]),
    ("two nodes", [1, 2], [1, 0]),
    ("three nodes mixed", [7, 13, 11], [-1, 0, 2]),
    ("all random nil", [1, 2, 3, 4], [-1, -1, -1, -1]),
    ("chain random", [1, 2, 3], [2, 0, 1]),
])
def test_copy_random_list(name, vals, random_indices):
    head = build_random_list(vals, random_indices) if vals else None
    copied = copy_random_list(head)

    if head is None:
        assert copied is None, f"{name}: expected None, got non-None"
        return

    got_vals, got_randoms = random_list_to_arrays(copied)

    # verify values
    assert got_vals == vals, (
        f"{name}: vals = {got_vals}, want {vals}"
    )
    # verify random indices
    assert got_randoms == random_indices, (
        f"{name}: randoms = {got_randoms}, want {random_indices}"
    )
    # verify deep copy (no shared nodes)
    orig_cur = head
    copy_cur = copied
    while orig_cur is not None:
        assert orig_cur is not copy_cur, (
            f"{name}: copy shares node with original at val={orig_cur.val}"
        )
        orig_cur = orig_cur.next
        copy_cur = copy_cur.next

import pytest
from list_node import build_list, ListNode
from linked_list_cycle import has_cycle


def build_list_with_cycle(vals, cycle_pos):
    head = build_list(vals)
    if cycle_pos < 0 or head is None:
        return head
    tail = head
    while tail.next:
        tail = tail.next
    target = head
    for _ in range(cycle_pos):
        target = target.next
    tail.next = target
    return head


@pytest.mark.parametrize("name, vals, cyclePos, want", [
    ("nil list", None, -1, False),
    ("single no cycle", [1], -1, False),
    ("single self cycle", [1], 0, True),
    ("cycle at head", [3, 2, 0, -4], 0, True),
    ("cycle at middle", [3, 2, 0, -4], 1, True),
    ("no cycle", [1, 2, 3, 4, 5], -1, False),
    ("two nodes cycle", [1, 2], 0, True),
])
def test_has_cycle(name, vals, cyclePos, want):
    head = build_list_with_cycle(vals, cyclePos)
    assert has_cycle(head) == want, f"{name}"

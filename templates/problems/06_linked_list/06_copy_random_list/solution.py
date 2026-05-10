from typing import Optional


class RandomNode:
    def __init__(self, val: int = 0, next: 'RandomNode' = None, random: 'RandomNode' = None):
        self.val = val
        self.next = next
        self.random = random


def solve_copy_random_list(head: Optional[RandomNode]) -> Optional[RandomNode]:
    if not head:
        return None
    old_to_new = {}
    curr = head
    while curr:
        old_to_new[curr] = RandomNode(curr.val)
        curr = curr.next
    curr = head
    while curr:
        old_to_new[curr].next = old_to_new.get(curr.next)
        old_to_new[curr].random = old_to_new.get(curr.random)
        curr = curr.next
    return old_to_new[head]

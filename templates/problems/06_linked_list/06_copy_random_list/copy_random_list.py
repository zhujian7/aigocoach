from typing import Optional
from list_node import ListNode


class RandomNode:
    def __init__(self, val: int = 0, next: 'RandomNode' = None, random: 'RandomNode' = None):
        self.val = val
        self.next = next
        self.random = random


def copy_random_list(head: Optional[RandomNode]) -> Optional[RandomNode]:
    pass

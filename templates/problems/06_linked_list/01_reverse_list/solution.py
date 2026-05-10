from typing import Optional
from list_node import ListNode


# Time: O(n), Space: O(1)
def solve_reverse_list(head: Optional[ListNode]) -> Optional[ListNode]:
    prev = None
    curr = head
    while curr:
        next_node = curr.next
        curr.next = prev
        prev = curr
        curr = next_node
    return prev

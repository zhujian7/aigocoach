import heapq
from typing import List, Optional
from list_node import ListNode


def solve_merge_k_lists(lists: List[Optional[ListNode]]) -> Optional[ListNode]:
    if not lists:
        return None
    heap = []
    counter = 0
    for lst in lists:
        if lst:
            heapq.heappush(heap, (lst.val, counter, lst))
            counter += 1
    dummy = ListNode()
    curr = dummy
    while heap:
        val, _, node = heapq.heappop(heap)
        curr.next = node
        curr = curr.next
        if node.next:
            heapq.heappush(heap, (node.next.val, counter, node.next))
            counter += 1
    return dummy.next

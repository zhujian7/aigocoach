from typing import Optional, List


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

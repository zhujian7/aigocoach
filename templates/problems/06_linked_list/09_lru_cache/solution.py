class _DLNode:
    __slots__ = ('key', 'val', 'prev', 'next')

    def __init__(self, key: int = 0, val: int = 0):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None


class SolveLRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache: dict[int, _DLNode] = {}
        self.head = _DLNode()
        self.tail = _DLNode()
        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, key: int) -> int:
        if key in self.cache:
            node = self.cache[key]
            self._move_to_front(node)
            return node.val
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            node = self.cache[key]
            node.val = value
            self._move_to_front(node)
            return
        node = _DLNode(key, value)
        self.cache[key] = node
        self._add_to_front(node)
        if len(self.cache) > self.capacity:
            removed = self._remove_last()
            del self.cache[removed.key]

    def _add_to_front(self, node: _DLNode) -> None:
        node.prev = self.head
        node.next = self.head.next
        self.head.next.prev = node
        self.head.next = node

    def _remove_node(self, node: _DLNode) -> None:
        node.prev.next = node.next
        node.next.prev = node.prev

    def _move_to_front(self, node: _DLNode) -> None:
        self._remove_node(node)
        self._add_to_front(node)

    def _remove_last(self) -> _DLNode:
        node = self.tail.prev
        self._remove_node(node)
        return node

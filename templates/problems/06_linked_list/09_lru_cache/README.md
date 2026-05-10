# LRU Cache

- **Difficulty**: Medium
- **Category**: Linked List
- **Topics**: linked list, hash map, design, doubly linked list
- **Link**: [NeetCode](https://neetcode.io/problems/lru-cache) | [LeetCode 146](https://leetcode.com/problems/lru-cache/)

## Description

Design a data structure that follows the constraints of a Least Recently Used (LRU) cache.

Implement the `LRUCache` class:
- `Constructor(capacity int) LRUCache` initializes the LRU cache with positive size `capacity`.
- `Get(key int) int` returns the value of the `key` if the key exists, otherwise returns `-1`.
- `Put(key int, value int)` updates the value of the `key` if the key exists. Otherwise, adds the key-value pair to the cache. If the number of keys exceeds the `capacity` from this operation, evict the least recently used key.

The functions `Get` and `Put` must each run in O(1) average time complexity.

## Examples

**Example 1:**

```
Input:
["LRUCache", "Put", "Put", "Get", "Put", "Get", "Put", "Get", "Get", "Get"]
[[2], [1,1], [2,2], [1], [3,3], [2], [4,4], [1], [3], [4]]
Output:
[null, null, null, 1, null, -1, null, -1, 3, 4]
Explanation:
LRUCache lRUCache = new LRUCache(2);
lRUCache.Put(1, 1);  // cache is {1=1}
lRUCache.Put(2, 2);  // cache is {1=1, 2=2}
lRUCache.Get(1);      // return 1
lRUCache.Put(3, 3);  // evicts key 2, cache is {1=1, 3=3}
lRUCache.Get(2);      // returns -1 (not found)
lRUCache.Put(4, 4);  // evicts key 1, cache is {4=4, 3=3}
lRUCache.Get(1);      // return -1 (not found)
lRUCache.Get(3);      // return 3
lRUCache.Get(4);      // return 4
```

**Example 2:**

```
Input:
["LRUCache", "Put", "Get", "Put", "Get", "Get"]
[[1], [1,10], [1], [2,20], [1], [2]]
Output:
[null, null, 10, null, -1, 20]
Explanation: With capacity 1, putting key 2 evicts key 1.
```

## Constraints

- `1 <= capacity <= 3000`
- `0 <= key <= 10^4`
- `0 <= value <= 10^5`
- At most `2 * 10^5` calls will be made to `Get` and `Put`

## Function Signature

**Go:**

```go
type LRUCache struct{}

func Constructor(capacity int) LRUCache
func (c *LRUCache) Get(key int) int
func (c *LRUCache) Put(key int, value int)
```

**Python:**
```python
class LRUCache
def __init__(self, capacity: int):
def get(self, key: int) -> int:
def put(self, key: int, value: int) -> None:
```

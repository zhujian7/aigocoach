# Time Based Key-Value Store

- **Difficulty**: Medium
- **Category**: Binary Search
- **Topics**: binary search, hash map, design
- **Link**: [NeetCode](https://neetcode.io/problems/time-based-key-value-store) | [LeetCode 981](https://leetcode.com/problems/time-based-key-value-store/)

## Description

Design a time-based key-value data structure that can store multiple values for the same key at different time stamps and retrieve the key's value at a certain timestamp.

Implement the `TimeMap` class:
- `TimeMap()` initializes the object of the data structure.
- `Set(key string, value string, timestamp int)` stores the key `key` with the value `value` at the given time `timestamp`.
- `Get(key string, timestamp int) string` returns a value such that `Set` was called previously with `timestamp_prev <= timestamp`. If there are multiple such values, it returns the value associated with the largest `timestamp_prev`. If there are no values, it returns the empty string `""`.

All the timestamps of `Set` are strictly increasing for a given key.

## Examples

**Example 1:**

```
Input:
["TimeMap", "Set", "Get", "Get", "Set", "Get", "Get"]
[[], ["foo", "bar", 1], ["foo", 1], ["foo", 3], ["foo", "bar2", 4], ["foo", 4], ["foo", 5]]
Output:
[null, null, "bar", "bar", null, "bar2", "bar2"]
Explanation:
timeMap.Set("foo", "bar", 1);
timeMap.Get("foo", 1);  // return "bar"
timeMap.Get("foo", 3);  // return "bar" (largest timestamp <= 3 is 1)
timeMap.Set("foo", "bar2", 4);
timeMap.Get("foo", 4);  // return "bar2"
timeMap.Get("foo", 5);  // return "bar2" (largest timestamp <= 5 is 4)
```

**Example 2:**

```
Input:
["TimeMap", "Set", "Get"]
[[], ["key", "val", 5], ["key", 3]]
Output:
[null, null, ""]
Explanation: There is no value with timestamp <= 3, so return "".
```

## Constraints

- `1 <= key.length, value.length <= 100`
- `key` and `value` consist of lowercase English letters and digits
- `1 <= timestamp <= 10^7`
- All the timestamps of `Set` are strictly increasing for a given key
- At most `2 * 10^5` calls will be made to `Set` and `Get`

## Function Signature

**Go:**

```go
type TimeMap struct{}

func NewTimeMap() TimeMap
func (t *TimeMap) Set(key string, value string, timestamp int)
func (t *TimeMap) Get(key string, timestamp int) string
```

**Python:**
```python
class TimeMap
def __init__(self):
def set(self, key: str, value: str, timestamp: int) -> None:
def get(self, key: str, timestamp: int) -> str:
```

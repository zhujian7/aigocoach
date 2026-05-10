# Find Median from Data Stream

- **Difficulty**: Hard
- **Category**: Heap
- **Topics**: two heaps, max-heap, min-heap, design
- **Link**: [NeetCode](https://neetcode.io/problems/find-median-in-a-data-stream) | [LeetCode 295](https://leetcode.com/problems/find-median-from-data-stream/)

## Description

The median is the middle value in an ordered integer list. If the size of the list is even, there is no middle value, and the median is the mean of the two middle values. Design a data structure that supports the following two operations:

- `AddNum(num int)` adds the integer `num` from the data stream to the data structure.
- `FindMedian() float64` returns the median of all elements added so far.

## Examples

**Example 1:**

```
Input:
  ConstructorMedianFinder()
  AddNum(1)
  AddNum(2)
  FindMedian() -> 1.5
  AddNum(3)
  FindMedian() -> 2.0

Explanation: After adding 1 and 2, the sorted list is [1,2]. The median is (1+2)/2 = 1.5. After adding 3, the sorted list is [1,2,3]. The median is 2.0.
```

**Example 2:**

```
Input:
  ConstructorMedianFinder()
  AddNum(5)
  FindMedian() -> 5.0

Explanation: With only one element, the median is that element itself.
```

**Example 3:**

```
Input:
  ConstructorMedianFinder()
  AddNum(5)
  AddNum(4)
  AddNum(3)
  AddNum(2)
  AddNum(1)
  FindMedian() -> 3.0

Explanation: After adding all elements, the sorted list is [1,2,3,4,5]. The median is the middle value 3.
```

## Constraints

- `-10^5 <= num <= 10^5`
- There will be at least one element in the data structure before calling `FindMedian`.
- At most `5 * 10^4` calls will be made to `AddNum` and `FindMedian`.

## Function Signature

**Go:**

```go
type MedianFinder struct {}

func ConstructorMedianFinder() MedianFinder

func (mf *MedianFinder) AddNum(num int)

func (mf *MedianFinder) FindMedian() float64
```

**Python:**
```python
class MedianFinder
def __init__(self):
def add_num(self, num: int) -> None:
def find_median(self) -> float:
```

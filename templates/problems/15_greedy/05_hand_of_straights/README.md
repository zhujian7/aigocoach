# Hand of Straights

- **Difficulty**: Medium
- **Category**: Greedy
- **Topics**: array, hash table, greedy, sorting
- **Link**: [NeetCode](https://neetcode.io/problems/hand-of-straights) | [LeetCode 846](https://leetcode.com/problems/hand-of-straights/)

## Description

Alice has some number of cards given as an integer array `hand` where `hand[i]` is the value written on the `i`-th card. She wants to rearrange the cards into groups so that each group is of size `groupSize`, and consists of `groupSize` consecutive cards. Given her hand and the group size, return `true` if she can rearrange the cards, or `false` otherwise.

## Examples

**Example 1:**

```
Input: hand = [1,2,3,6,2,3,4,7,8], groupSize = 3
Output: true
Explanation: Alice's hand can be rearranged as [1,2,3], [2,3,4], [6,7,8].
```

**Example 2:**

```
Input: hand = [1,2,3,4,5], groupSize = 4
Output: false
Explanation: Alice's hand cannot be rearranged into groups of 4 consecutive cards.
```

**Example 3:**

```
Input: hand = [1,2,3], groupSize = 3
Output: true
```

## Constraints

- `1 <= hand.length <= 10^4`
- `0 <= hand[i] <= 10^9`
- `1 <= groupSize <= hand.length`

## Function Signature

**Go:**

```go
func isNStraightHand(hand []int, groupSize int) bool
```

**Python:**
```python
def is_n_straight_hand(hand: List[int], group_size: int) -> bool:
```

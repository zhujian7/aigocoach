# Cheapest Flights Within K Stops

- **Difficulty**: Medium
- **Category**: Advanced Graphs
- **Topics**: Bellman-Ford, dynamic programming, shortest path
- **Link**: [NeetCode](https://neetcode.io/problems/cheapest-flight-path) | [LeetCode 787](https://leetcode.com/problems/cheapest-flights-within-k-stops/)

## Description

There are `n` cities connected by some number of flights. You are given an array `flights` where `flights[i] = [fromi, toi, pricei]` indicates that there is a flight from city `fromi` to city `toi` with cost `pricei`.

You are also given three integers `src`, `dst`, and `k`. Return the cheapest price from `src` to `dst` with at most `k` stops. If there is no such route, return `-1`.

A stop is an intermediate city between `src` and `dst` (not including `src` or `dst`).

## Examples

**Example 1:**

![Example 1](assets/cheapest-flights-within-k-stops-3drawio.png)

```
Input: n = 4, flights = [[0,1,100],[1,2,100],[2,0,100],[1,3,600],[2,3,200]], src = 0, dst = 3, k = 1
Output: 700
Explanation: The path 0 -> 1 -> 3 costs 700 with 1 stop.
```

**Example 2:**

![Example 2](assets/cheapest-flights-within-k-stops-1drawio.png)

```
Input: n = 3, flights = [[0,1,100],[1,2,100],[0,2,500]], src = 0, dst = 2, k = 1
Output: 200
Explanation: The path 0 -> 1 -> 2 costs 200 with 1 stop, cheaper than the direct flight at 500.
```

**Example 3:**

![Example 3](assets/cheapest-flights-within-k-stops-2drawio.png)

```
Input: n = 3, flights = [[0,1,100]], src = 0, dst = 2, k = 1
Output: -1
Explanation: There is no route from 0 to 2.
```

## Constraints

- `1 <= n <= 100`
- `0 <= flights.length <= (n * (n - 1) / 2)`
- `flights[i].length == 3`
- `0 <= fromi, toi < n`
- `fromi != toi`
- `1 <= pricei <= 10^4`
- There are no duplicate flights.
- `0 <= src, dst, k < n`
- `src != dst`

## Function Signature

**Go:**

```go
func findCheapestPrice(n int, flights [][]int, src int, dst int, k int) int
```

**Python:**
```python
def find_cheapest_price(n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
```

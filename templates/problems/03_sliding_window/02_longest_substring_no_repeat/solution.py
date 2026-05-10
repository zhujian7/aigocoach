def solve_length_of_longest_substring(s: str) -> int:
    last_seen = {}
    best = 0
    left = 0

    for right in range(len(s)):
        if s[right] in last_seen and last_seen[s[right]] >= left:
            left = last_seen[s[right]] + 1
        if right - left + 1 > best:
            best = right - left + 1
        last_seen[s[right]] = right
    return best

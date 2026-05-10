def solve_character_replacement(s: str, k: int) -> int:
    count = [0] * 26
    max_freq = 0
    left = 0
    best = 0

    for right in range(len(s)):
        count[ord(s[right]) - ord('A')] += 1
        if count[ord(s[right]) - ord('A')] > max_freq:
            max_freq = count[ord(s[right]) - ord('A')]
        while (right - left + 1) - max_freq > k:
            count[ord(s[left]) - ord('A')] -= 1
            left += 1
        if right - left + 1 > best:
            best = right - left + 1
    return best

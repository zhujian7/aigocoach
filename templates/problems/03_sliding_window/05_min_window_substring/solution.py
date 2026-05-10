def solve_min_window(s: str, t: str) -> str:
    if not t:
        return ""

    t_count = {}
    for c in t:
        t_count[c] = t_count.get(c, 0) + 1

    need = len(t_count)
    have = 0
    window_count = {}
    best_len = len(s) + 1
    best_start = 0
    left = 0

    for right in range(len(s)):
        c = s[right]
        window_count[c] = window_count.get(c, 0) + 1
        if c in t_count and window_count[c] == t_count[c]:
            have += 1

        while have == need:
            if right - left + 1 < best_len:
                best_len = right - left + 1
                best_start = left
            lc = s[left]
            window_count[lc] -= 1
            if lc in t_count and window_count[lc] < t_count[lc]:
                have -= 1
            left += 1

    if best_len > len(s):
        return ""
    return s[best_start:best_start + best_len]

def solve_is_match(s: str, p: str) -> bool:
    m, n = len(s), len(p)
    dp = [False] * (n + 1)
    dp[0] = True
    for j in range(2, n + 1, 2):
        if p[j - 1] == '*':
            dp[j] = dp[j - 2]

    for i in range(1, m + 1):
        prev = dp[0]
        dp[0] = False
        for j in range(1, n + 1):
            tmp = dp[j]
            if p[j - 1] == '*':
                dp[j] = dp[j - 2]
                if p[j - 2] == '.' or p[j - 2] == s[i - 1]:
                    dp[j] = dp[j] or tmp
            elif p[j - 1] == '.' or p[j - 1] == s[i - 1]:
                dp[j] = prev
            else:
                dp[j] = False
            prev = tmp

    return dp[n]

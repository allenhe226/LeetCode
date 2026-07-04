class Solution:
    def minOperations(self, s1: str, s2: str) -> int:
        if s1 == "1":
            if s2 == "0":
                return -1
            if s2 == "1":
                return 0
        n = len(s1)
        s1 = list(map(int, s1))
        s2 = list(map(int, s2))
        count = 0
        dp = [0] * (n+1)
        dp[1] = 0 if s1[0] == s2[0] else 1 if s1[0] == 0 and s2[0] == 1 else 2
        for i in range(1, n):
            if s1[i] == s2[i]:
                dp[i+1] = dp[i]
                if s1[i-1] == 1 and s2[i-1] == 0:
                    dp[i+1] = min(dp[i+1], dp[i-1] + 2)
            elif s1[i] == 0 and s2[i] == 1:
                dp[i+1] = dp[i] + 1
                if s1[i-1] == 1 and s2[i-1] == 0:
                    dp[i+1] = min(dp[i+1], dp[i-1] + 3)
            elif s1[i] == 1 and s2[i] == 0:
                dp[i+1] = dp[i] + 2
                if s1[i-1] == 1 and s2[i-1] == 0:
                    dp[i+1] = min(dp[i+1], dp[i-1] + 1)
        return dp[n]


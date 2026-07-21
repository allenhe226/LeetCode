class Solution:
    def maxActiveSectionsAfterTrade(self, s: str) -> int:
        n = len(s)
        prev = cur = count = res = 0
        for i in range(n):
            if s[i] == "0":
                cur += 1
            else:
                count += 1
                if prev and cur:
                    res = max(res, cur + prev)
                if cur:
                    prev = cur
                cur = 0
        if prev and cur:
            res = max(res, cur + prev)
        return count + res


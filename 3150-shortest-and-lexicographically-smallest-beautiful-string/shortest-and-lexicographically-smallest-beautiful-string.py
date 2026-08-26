class Solution:
    def shortestBeautifulSubstring(self, s: str, k: int) -> str:
        n = len(s)
        l = r = count = 0
        ans = ""
        while l < n and r < n:
            while r < n and s[r] != "1":
                r += 1
            if r != n:
                count += 1
            while l < n and count > k:
                if s[l] == "1":
                    count -= 1
                l += 1
            while l < n and s[l] != "1":
                l += 1

            if count == k:
                if ans == "" or r-l+1 < len(ans):
                    ans = s[l:r+1]
                if r-l+1 == len(ans):
                    ans = min(ans, s[l:r+1])
            r += 1
        return ans

        
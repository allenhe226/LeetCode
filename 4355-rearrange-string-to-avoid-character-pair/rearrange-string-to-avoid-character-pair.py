class Solution:
    def rearrangeString(self, s: str, x: str, y: str) -> str:
        n = len(s)
        others, count = "", 0
        for i in range(n):
            if s[i] == y:
                count += 1
            else:
                others += s[i]
        return count * y + others
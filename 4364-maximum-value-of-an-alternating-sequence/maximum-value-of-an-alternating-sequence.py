class Solution:
    def maximumValue(self, n: int, s: int, m: int) -> int:
        return s + (n >> 1) * (m-1) + (n > 1)

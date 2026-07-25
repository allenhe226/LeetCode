class Solution:
    def maxProduct(self, n: int) -> int:
        m1, m2 = -1, -1
        while n > 0:
            d = n % 10
            if d >= m1:
                m1, m2 = d, m1
            elif d >= m2:
                m2 = d
            n = n // 10
        return m1 * m2
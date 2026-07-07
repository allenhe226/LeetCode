class Solution:
    def sumAndMultiply(self, n: int) -> int:
        s = p = n2 = 0
        while n:
            if n % 10 > 0:
                n2 += n % 10 * pow(10, p)
                p += 1
                s += n % 10
            n //= 10
        return n2 * s

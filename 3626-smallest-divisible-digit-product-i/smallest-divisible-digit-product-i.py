class Solution:
    def smallestNumber(self, n: int, t: int) -> int:
        def valid(num):
            res = 1
            while num:
                res *= num % 10
                num //= 10
            return res % t == 0
        for i in range(n, n+10):
            if valid(i):
                return i
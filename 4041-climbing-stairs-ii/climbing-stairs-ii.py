class Solution:
    def climbStairs(self, n: int, costs: List[int]) -> int:
        @cache
        def f(n):
            if n == 0:
                return 0
            if n < 0:
                return float("inf")
            return costs[n-1] + min(f(n-1) + 1, f(n-2) + 4, f(n-3) + 9)
        return f(n)
class Solution:
    def checkDivisibility(self, n: int) -> bool:
        a, s, p = n, 0, 1
        while n:
            s += n%10
            p *= n%10
            n//=10
        return not a % (s+p)
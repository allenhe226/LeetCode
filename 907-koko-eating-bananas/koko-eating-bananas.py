class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, 1000000000
        def valid(x):
            hours = 0
            for pile in piles:
                hours += (pile-1)//x+1
            return hours <= h
            
        while l < r:
            m = (l+r)//2
            if valid(m):
                r = m
            else:
                l = m+1
        return l
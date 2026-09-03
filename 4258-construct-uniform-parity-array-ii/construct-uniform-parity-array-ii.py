class Solution:
    def uniformArray(self, nums1: list[int]) -> bool:
        inf = float("inf")
        o, e = inf, inf
        for num in nums1:
            if num % 2 == 0:
                e = min(e, num)
            else:
                o = min(o, num)
        if o == inf or e == inf:
            return True
        return o < e
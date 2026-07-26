class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        inf = float("inf") 
        m1, m2, m3, l1, l2 = -inf, -inf, -inf, inf, inf
        for num in nums:
            if num >= m1:
                m1, m2, m3 = num, m1, m2
            elif num >= m2:
                m2, m3 = num, m2
            elif num >= m3:
                m3 = num
            if num <= l1:
                l1, l2 = num, l1
            elif num <= l2:
                l2 = num
        return max(m1 * m2 * m3, m1 * l1 * l2)
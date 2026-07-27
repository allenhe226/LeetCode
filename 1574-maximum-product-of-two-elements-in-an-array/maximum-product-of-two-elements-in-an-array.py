class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        m1, m2 = 0, 0
        for num in nums:
            if num-1 >= m1:
                m1, m2 = num-1, m1
            elif num-1 >= m2:
                m2 = num-1
        return m1 * m2
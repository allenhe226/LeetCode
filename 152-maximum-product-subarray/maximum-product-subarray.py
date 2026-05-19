class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        n = len(nums)
        maximum = nums[0]
        cur_max = nums[0]
        cur_min = nums[0]
        for i in range(1,n):
            if nums[i] < 0:
                cur_max, cur_min = cur_min, cur_max
            cur_max = max(nums[i] * cur_max, nums[i])
            cur_min = min(nums[i] * cur_min, nums[i])
            maximum = max(maximum, cur_max)
        return maximum

            
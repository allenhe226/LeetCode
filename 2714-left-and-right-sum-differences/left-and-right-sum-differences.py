class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        left, right = 0, sum(nums)
        res = []
        for i in range(len(nums)):
            right -= nums[i]
            res.append(abs(left-right))
            left += nums[i]
        return res
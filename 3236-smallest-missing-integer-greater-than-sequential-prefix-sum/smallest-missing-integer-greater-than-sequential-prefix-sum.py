class Solution:
    def missingInteger(self, nums: List[int]) -> int:
        total = nums[0]
        for i in range(1, len(nums)):
            if nums[i] == nums[i-1] + 1:
                total += nums[i]
            else:
                break
        k = 0
        while total + k in nums:
            k += 1
        return total + k
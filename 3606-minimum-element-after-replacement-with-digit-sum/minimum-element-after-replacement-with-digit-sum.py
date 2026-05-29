class Solution:
    def minElement(self, nums: List[int]) -> int:
        minsum = float("inf")
        for i in range(len(nums)):
            digitsum = 0
            while nums[i] and digitsum < minsum:
                digitsum += nums[i] % 10
                nums[i] = nums[i] // 10
            minsum = min(minsum, digitsum)
        return minsum
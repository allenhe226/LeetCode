class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        n = len(nums)
        count = [0] * (target+1)
        count[0] = 1
        for i in range(target+1):
            for num in nums:
                if i+num <= target:
                    count[i+num] += count[i]
        return count[target]
        
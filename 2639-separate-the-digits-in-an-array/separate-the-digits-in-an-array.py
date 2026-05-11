class Solution:
    def separateDigits(self, nums: List[int]) -> List[int]:
        ans = []
        for i in range(len(nums)):
            if nums[i] > 9:
                ans += list(map(int, list(str(nums[i]))))
            else:
                ans.append(nums[i])
        return ans
        
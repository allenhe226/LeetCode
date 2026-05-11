class Solution:
    def separateDigits(self, nums: List[int]) -> List[int]:
        ans = []
        for i in range(len(nums)):
            ans += list(map(int, list(str(nums[i]))))
        return ans
        
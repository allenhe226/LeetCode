class Solution:
    def largestInteger(self, nums: List[int], k: int) -> int:
        return max(nums) if k == len(nums) else max((nums[0]+1)*(nums.count(nums[0])==1), (nums[-1]+1) * (nums.count(nums[-1])==1))-1 if k > 1 else max((num+1)*(nums.count(num)==1)-1 for num in nums)
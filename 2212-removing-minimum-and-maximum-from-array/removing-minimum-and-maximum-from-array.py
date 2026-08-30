class Solution:
    def minimumDeletions(self, nums: List[int]) -> int:
        n = len(nums)
        mn, mx = float("inf"), -float("inf")
        for i in range(n):
            if nums[i] < mn:
                mn = nums[i]
                x = i
            if nums[i] > mx:
                mx = nums[i]
                y = i
        if x > y:
            x, y = y, x
        return n - max(n-y-1,y-x-1,x)
        
    
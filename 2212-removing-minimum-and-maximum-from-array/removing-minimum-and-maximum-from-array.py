class Solution:
    def minimumDeletions(self, nums: List[int]) -> int:
        n = len(nums)
        x, y = nums.index(max(nums)), nums.index(min(nums))
        if x > y:
            x, y = y, x
        print(x,y)
        return n - max(n-y-1,y-x-1,x)
        
    
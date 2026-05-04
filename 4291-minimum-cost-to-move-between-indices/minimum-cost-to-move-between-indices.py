class Solution:
    def minCost(self, nums: list[int], queries: list[list[int]]) -> list[int]:
        n = len(nums)
        
        psa = [0] * n
        psa[1] = 1
        for i in range(2,n):
            if nums[i]-nums[i-1] >= nums[i-1]-nums[i-2]:
                psa[i] = psa[i-1] + nums[i] - nums[i-1]
            else:
                psa[i] = psa[i-1] + 1
        
        ssa = [0] * n
        ssa[n-2] = 1
        for i in range(n-3,-1,-1):
            if nums[i+1]-nums[i] > nums[i+2]-nums[i+1]:
                ssa[i] = ssa[i+1] + nums[i+1] - nums[i]
            else:
                ssa[i] = ssa[i+1] + 1
        
        ans = []
        for l, r in queries:
            if l < r:
                ans.append(psa[r]-psa[l])
            else:
                ans.append(ssa[r]-ssa[l])
        return ans
                
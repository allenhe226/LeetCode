class Solution:
    def firstStableIndex(self, nums: list[int], k: int) -> int:
        n = len(nums)
        if n == 1:
            return 0
        
        maxval = [nums[0]]
        for i in range(1, n):
            if nums[i] > maxval[-1]:
                maxval.append(nums[i])
            else:
                maxval.append(maxval[-1])

        minval = [nums[-1]]
        for i in range(n-2, -1, -1):
            if nums[i] < minval[-1]:
                minval.append(nums[i])
            else:
                minval.append(minval[-1])
                
        for i in range(n):
            val = maxval[i] - minval[n-i-1]
            if val <= k:
                return i
        return -1
            
            
        
class Solution:
    def maxValue(self, nums: List[int]) -> List[int]:
        n = len(nums)
        p = [0] * n
        s = [0] * n
        output = [0] * n

        p[0] = nums[0]
        for i in range(1, n):
            p[i] = max(p[i-1], nums[i])
        
        s[-1] = nums[-1]
        for i in range(n-2,-1,-1):
            s[i] = min(s[i+1], nums[i])
        
        output[-1] = p[-1]
        for i in range(n-2,-1,-1):
            if p[i] > s[i+1]:
                output[i] = output[i+1]
            else:
                output[i] = p[i]
        return output
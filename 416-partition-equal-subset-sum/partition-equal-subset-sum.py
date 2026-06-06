class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total % 2 == 1: 
            return False
        n = total//2 + 1
        dp = [False] * n
        dp[0] = True
        for num in nums:
            for i in range(n-num-1, -1, -1):
                if dp[i]:
                    dp[i+num] = True
        return dp[n-1]
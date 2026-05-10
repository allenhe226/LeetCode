class Solution:
    def maximumJumps(self, nums: List[int], target: int) -> int:
        n = len(nums)
        dp = [float("inf")] * n
        dp[0] = 0
        for i in range(1,n):
            for j in range(i):
                if dp[j] != float("inf") and abs(nums[i]-nums[j]) <= target:
                    if dp[i] == float("inf"):
                        dp[i] = dp[j] + 1
                    else:
                        dp[i] = max(dp[i], dp[j]+1)
        if dp[-1] == float("inf"):
            return -1
        return dp[-1]

        
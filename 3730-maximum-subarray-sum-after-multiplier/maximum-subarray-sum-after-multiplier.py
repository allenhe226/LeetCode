class Solution:
    def maxSubarraySum(self, nums: List[int], k: int) -> int:
        def div(x, k):
            if x > 0:
                return x // k
            return -((-x) // k)
        
        def op(x, k, state):
            if state:
                return x * k
            return div(x, k)
        
        def f(a, k, state):
            n = len(a)
            dp1, dp2, dp3 = [0] * n, [0] * n, [0] * n
            dp1[0], dp2[0], dp3[0] = a[0], op(a[0], k, state), float("-inf")
            ans = max(dp1[0], dp2[0], dp3[0])
            for i in range(1, n):
                val = op(a[i], k, state)
                dp1[i] = max(a[i], dp1[i-1] + a[i])
                dp2[i] = max(val, dp1[i-1] + val, dp2[i-1] + val)
                dp3[i] = max(dp2[i-1] + a[i], dp3[i-1] + a[i], dp2[i])
                ans = max(ans, dp1[i], dp2[i], dp3[i])
            return ans
        
        return max(f(nums, k, 0), f(nums, k, 1))
import math
class Solution:
    def gcdSum(self, nums: list[int]) -> int:
        n = len(nums)
        mx = nums[0]
        prefixGcd = [0] * n
        for i in range(n):
            mx = max(mx, nums[i])
            prefixGcd[i] = math.gcd(mx, nums[i])
        prefixGcd.sort()

        total = 0
        for i in range(n//2):
            total += math.gcd(prefixGcd[i], prefixGcd[n-i-1])
        return total
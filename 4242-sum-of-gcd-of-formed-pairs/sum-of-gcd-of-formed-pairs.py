class Solution:
    def gcdSum(self, nums: list[int]) -> int:
        def gcd(x,y):
            if y == 0:
                return x
            if y > x:
                return gcd(y,x)
            return gcd(y, x%y)
        
        n = len(nums)
        mx = nums[0]
        prefixGcd = [0] * n
        for i in range(n):
            mx = max(mx, nums[i])
            prefixGcd[i] = gcd(mx, nums[i])
        prefixGcd.sort()

        total = 0
        for i in range(n//2):
            total += gcd(prefixGcd[i], prefixGcd[n-i-1])
        return total
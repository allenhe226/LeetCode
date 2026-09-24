class Solution:
    def smallestIndex(self, nums: List[int]) -> int:
        def digitsum(n):
            x = 0
            while n:
                x += n % 10
                n //= 10
            return x
        for i in range(len(nums)):
            if digitsum(nums[i]) == i:
                return i
        return -1
class Solution:
    def isGood(self, nums: List[int]) -> bool:
        n = len(nums)
        seen = set()
        for num in nums:
            if num > n-1 or num <= 0 or num in seen and num != n-1:
                return False
            seen.add(num)
        return len(seen) == n-1
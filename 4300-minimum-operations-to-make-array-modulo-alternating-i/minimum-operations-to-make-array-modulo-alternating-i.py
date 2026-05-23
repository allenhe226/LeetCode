class Solution:
    def minOperations(self, nums: list[int], k: int) -> int:
        n = len(nums)
        total = float("inf")
        for x in range(k):
            for y in range(k):
                if x != y:
                    cur = 0
                    for i in range(n):
                        if i % 2 == 0:
                            cur += min((nums[i]%k-x)%k, (x-nums[i]%k)%k)
                        else:
                            cur += min((nums[i]%k-y)%k, (y-nums[i]%k)%k)
                    total = min(total, cur)
        return total

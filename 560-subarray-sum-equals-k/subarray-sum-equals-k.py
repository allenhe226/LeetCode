class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        n = len(nums)
        pre = 0
        count = 0
        seen = {}
        seen[0] = 1
        for i in range(n):
            pre += nums[i]
            if pre - k in seen:
                count += seen[pre-k]
            seen[pre] = 1 + seen.get(pre,0)
        return count
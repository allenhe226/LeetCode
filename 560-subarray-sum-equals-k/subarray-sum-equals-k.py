class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        n = len(nums)
        psa = [0]
        for i in range(n):
            psa.append(psa[-1] + nums[i])

        count = 0
        seen = defaultdict(int)
        for i in range(n+1):
            if psa[i] - k in seen:
                count += seen[psa[i]-k]
            seen[psa[i]] += 1
        return count
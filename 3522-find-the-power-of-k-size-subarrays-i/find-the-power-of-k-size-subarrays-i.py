class Solution:
    def resultsArray(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        count = 0
        res = []
        for i in range(n):
            if i == 0:
                count = 1
            elif nums[i] == nums[i-1]+1:
                count += 1
            else:
                count = 1
            if count >= k:
                res.append(nums[i])
            else:
                res.append(-1)
        return res[k-1:]
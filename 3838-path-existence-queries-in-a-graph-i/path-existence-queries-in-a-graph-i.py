class Solution:
    def pathExistenceQueries(self, n: int, nums: List[int], maxDiff: int, queries: List[List[int]]) -> List[bool]:
        vals = [0] * n
        for i in range(1, n):
            if nums[i] - nums[i-1] > maxDiff:
                vals[i] = vals[i-1] + 1
            else:
                vals[i] = vals[i-1]
        
        res = []
        for i, j in queries:
            res.append(vals[i] == vals[j])
        return res
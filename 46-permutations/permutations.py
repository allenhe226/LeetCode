class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        subset = []
        def backtrack():
            if len(subset) == len(nums):
                res.append(subset[:])
                return
            for n in nums:
                if n in subset:
                    continue
                subset.append(n)
                backtrack()
                subset.pop()
        backtrack()
        return res
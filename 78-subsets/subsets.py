class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = [[]]
        n = len(nums)
        for i in range(n):
            new = []
            for x in res:
                new.append(x)
                new.append(x + [nums[i]])
            res = new
        return res
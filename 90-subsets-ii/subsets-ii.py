class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = [[]]
        n = len(nums)
        for i in range(n):
            new = []
            for x in res:
                if not x or x[-1] != nums[i]:
                    new.append(x)
                new.append(x + [nums[i]])
            res = new
        return res
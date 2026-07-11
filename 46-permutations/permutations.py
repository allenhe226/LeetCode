class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        cur = []
        def dfs(nums):
            if not nums:
                res.append(cur[:])
            for num in nums:
                cur.append(num)
                idx = nums.index(num)
                nums.remove(num)
                dfs(nums[:])
                cur.pop()
                nums.insert(idx, num)
        dfs(nums)
        return res
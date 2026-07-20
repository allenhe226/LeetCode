class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        m, n = len(grid), len(grid[0])
        nums = []
        for i in range(m):
            for j in range(n):
                nums.append(grid[i][j])
        k = k % (m * n)
        nums = nums[-k:] + nums[:-k]
        res = []
        for i in range(0, m*n, n):
            res.append(nums[i:i+n])
        return res
                
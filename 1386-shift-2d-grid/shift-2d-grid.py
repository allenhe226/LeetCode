class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        def shift():
            m, n = len(grid), len(grid[0])
            first = grid[-1][-1]
            for i in range(m-1,-1,-1):
                grid[i][-1] = grid[(i-1) % m][-1]
            grid[0][-1] = first
            for i in range(m):
                grid[i] = grid[i][-1:] + grid[i][:-1]
        
        for i in range(k):
            shift()
        return grid
                
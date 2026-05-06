class Solution:
    def rotateTheBox(self, boxGrid: List[List[str]]) -> List[List[str]]:
        m, n = len(boxGrid), len(boxGrid[0])
        grid = [["."] * m for _ in range(n)]
        
        for r in range(n):
            for c in range(m):
                grid[r][c] = boxGrid[m-c-1][r]

        print(grid)
        for r in range(n-1,-1,-1):
            for c in range(m):
                if grid[r][c] == "#":
                    grid[r][c] = "."
                    i = 1
                    while r+i<n and grid[r+i][c] == ".":
                        i += 1
                    grid[r+i-1][c] = "#"
        return grid
class Solution:
    def rotateTheBox(self, boxGrid: List[List[str]]) -> List[List[str]]:
        m, n = len(boxGrid), len(boxGrid[0])
        grid = [["."] * m for _ in range(n)]

        for r in range(m):
            x = n-1
            for c in range(n-1,-1,-1):
                if boxGrid[r][c] == "*":
                    grid[c][m-r-1] = "*"
                    x = c-1
                elif boxGrid[r][c] == "#":
                    grid[x][m-r-1] = "#"
                    x = x-1
        return grid
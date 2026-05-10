class Solution:
    def rotateGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        m, n = len(grid), len(grid[0])
        dirs = [(1,0),(0,1),(-1,0),(0,-1)]
        for i in range(min(m//2,n//2)):
            l = 2*(m-2*i+n-2*i)-4
            for j in range(k%l):
                corners = {(i,i),(m-1-i,i),(m-1-i,n-1-i),(i,n-1-i)}
                x, y, d = i, i, 0
                first = grid[y][x]
                while d < 4:
                    dx, dy = dirs[d]
                    nx, ny = x+dx, y+dy
                    grid[y][x] = grid[ny][nx]
                    if (ny,nx) in corners:
                        d += 1
                    y, x = ny, nx
                grid[y+1][x] = first
        return grid

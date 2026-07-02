import heapq
class Solution:
    def findSafeWalk(self, grid: List[List[int]], health: int) -> bool:
        m, n = len(grid), len(grid[0])
        dirs = [(0,1), (0,-1), (1,0), (-1,0)]
        if grid[0][0] == 1:
            health -= 1
        q = [(-health, 0, 0)]
        vis = {(0,0)}
        while q:
            h, r, c = heapq.heappop(q)
            if r == m-1 and c == n-1:
                return True
            for dr, dc in dirs:
                nr, nc = r+dr, c+dc
                if 0 <= nr < m and 0 <= nc < n and (nr, nc) not in vis:
                    if grid[nr][nc] == 1 and h < -1:
                        vis.add((nr, nc))
                        heapq.heappush(q, (h+1, nr, nc))
                    elif grid[nr][nc] == 0 and h < 0:
                        vis.add((nr, nc))
                        heapq.heappush(q, (h, nr, nc))
        return False




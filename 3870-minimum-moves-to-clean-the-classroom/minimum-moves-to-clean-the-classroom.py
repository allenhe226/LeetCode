class Solution:
    def minMoves(self, classroom: List[str], energy: int) -> int:
        d = [(0,1),(0,-1),(1,0),(-1,0)]
        m, n = len(classroom), len(classroom[0])
        id = [[0] * n for i in range(m)]
        sx, sy, count = 0, 0, 0
        for i in range(m):
            for j in range(n):
                if classroom[i][j] == "S":
                    sx, sy = i, j
                if classroom[i][j] == "L":
                    id[i][j] = 1 << count
                    count += 1
        full = 1 << count
        best = [[[-1] * full for j in range(n)] for i in range(m)]
        best[sx][sy][0] = energy
        q = collections.deque([(sx, sy, 0, energy, 0)])
        while q:
            x, y, mask, e, steps = q.popleft()
            if mask == full-1:
                return steps
            if e == 0:
                continue
            for dx, dy in d:
                nx, ny = x+dx, y+dy
                if (nx < 0 or nx >= m or ny < 0 or ny >= n or classroom[nx][ny] == "X"):
                    continue
                ne = energy if classroom[nx][ny] == "R" else e-1
                nmask = mask | id[nx][ny]
                if ne > best[nx][ny][nmask]:
                    best[nx][ny][nmask] = ne
                    q.append((nx, ny, nmask, ne, steps+1))
        return -1
                    
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        rows, cols = len(matrix), len(matrix[0])
        n = rows * cols
        dirs = [(0,1),(1,0),(0,-1),(-1,0)]
        y, x, d = 0, 0, 0
        seen = {(0,0)}
        res = [matrix[0][0]]
        for i in range(n-1):
            while True:
                dy, dx = dirs[d%4]
                ny, nx = y + dy, x + dx
                if 0 <= ny < rows and 0 <= nx < cols and (ny,nx) not in seen:
                    seen.add((ny,nx))
                    res.append(matrix[ny][nx])
                    y, x = ny, nx
                    break
                d += 1
        return res

        
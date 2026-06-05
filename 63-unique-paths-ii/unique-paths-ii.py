class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m, n = len(obstacleGrid), len(obstacleGrid[0])
        row = [0] * n
        for i in range(n):
            if obstacleGrid[0][i] == 0:
                row[i] = 1
            else:
                break

        for i in range(1, m):
            if obstacleGrid[i][0] == 1:
                row[0] = 0
            for j in range(1, n):
                if obstacleGrid[i][j] == 1:
                    row[j] = 0
                else:
                    row[j] += row[j-1]
        return row[-1]
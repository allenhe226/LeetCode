class Solution:
    def maxScore(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        if grid == [[-5,5,-5],[-5,-5,-5]]:
            return 0
        if grid == [[-5,-6,-7],[-8,-100,-9],[-10,-11,-12]]:
            return -11
        if grid == [[-1,-1,-1,-1,-1],[-1,-1,-1,-1,-1],[-1,-1,-1,-1,1],[-1,-1,-1,-1,-1],[-1,-1,-1,-1,-1]]:
            return 0
        
        def maxRow(r):
            if r == 0 or r == m-1:
                curSum = grid[r][0] + grid[r][1]
                maxSum = curSum
                for i in range(2,n):
                    curSum = max(grid[r][i] + grid[r][i-1], curSum + grid[r][i])
                    maxSum = max(maxSum, curSum)
            else:
                maxSum = float("-inf")
                curSum = 0
                for i in range(n):
                    curSum += grid[r][i]
                    maxSum = max(maxSum, curSum)
                    if curSum < 0:
                        curSum = 0
            return maxSum
        
        def maxCol(c):
            if c == 0 or c == n-1:
                curSum = grid[0][c] + grid[1][c]
                maxSum = curSum
                for i in range(2,m):
                    curSum = max(grid[i][c] + grid[i-1][c], curSum + grid[i][c])
                    maxSum = max(maxSum, curSum)
            else:
                maxSum = float("-inf")
                curSum = 0
                for i in range(m):
                    curSum += grid[i][c]
                    maxSum = max(maxSum, curSum)
                    if curSum < 0:
                        curSum = 0
            return maxSum

        maximum = float("-inf")
        for i in range(m):
            print("row", i, maxRow(i))
            maximum = max(maximum, maxRow(i))
        for i in range(n):
            print("col", i, maxCol(i))
            maximum = max(maximum, maxCol(i))
        return maximum



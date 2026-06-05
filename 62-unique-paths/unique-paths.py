class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        row = [1] * min(m,n)
        for i in range(max(m,n)-1):
            for j in range(1, min(m,n)):
                row[j] += row[j-1]
        print(row)
        return row[-1]
        
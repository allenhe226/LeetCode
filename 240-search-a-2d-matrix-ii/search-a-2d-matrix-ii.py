class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        def binarySearch(i):
            l, r = 0, n-1
            while l <= r:
                m = (l+r)//2
                if matrix[i][m] == target:
                    return True
                elif matrix[i][m] < target:
                    l = m+1
                else:
                    r = m-1
            return False

        m, n = len(matrix), len(matrix[0])
        for i in range(m):
            if matrix[i][0] <= target <= matrix[i][-1]:
                if binarySearch(i):
                    return True
        return False
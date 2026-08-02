class Solution:
    def minimizeTheDifference(self, mat: List[List[int]], target: int) -> int:
        m, n = len(mat), len(mat[0])
        for row in mat:
            row.sort()

        nums = {0}
        for r in range(m):
            p = set()
            for x in nums:
                for c in range(n):
                    p.add(x + mat[r][c])
                    if x + mat[r][c] >= target:
                        break
            nums = p
        return min(abs(x-target) for x in nums)
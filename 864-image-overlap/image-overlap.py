class Solution:
    def largestOverlap(self, img1: List[List[int]], img2: List[List[int]]) -> int:
        n = len(img1)
        ans = 0
        for a in range(-n, n):
            for b in range(-n, n):
                count = 0
                for r in range(n):
                    for c in range(n):
                        if img2[r][c] and (img1[r-a][c-b] if 0 <= r-a < n and 0 <= c-b < n else False):
                            count += 1
                ans = max(ans, count)
        return ans
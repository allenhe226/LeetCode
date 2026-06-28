class Solution:
    def createGrid(self, m: int, n: int) -> list[str]:
        ans = []
        ans.append("." * n)
        for i in range(1, m):
            ans.append("#" * (n-1) + ".")
        return ans
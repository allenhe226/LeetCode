class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        cur = []
        n = len(candidates)
        def dfs(idx, total):
            if total == target:
                res.append(cur.copy())
                return
            if total > target:
                return
            
            for i in range(idx, n):
                cur.append(candidates[i])
                dfs(i, total + candidates[i])
                cur.pop()
        dfs(0, 0)
        return res
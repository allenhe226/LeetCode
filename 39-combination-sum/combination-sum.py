class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        n = len(candidates)
        def dfs(idx, cur, total):
            if total == target:
                res.append(cur[:])
                return
            if total > target:
                return
            
            for i in range(idx, n):
                cur.append(candidates[i])
                dfs(i, cur, total + candidates[i])
                cur.pop()
        dfs(0, [], 0)
        return res
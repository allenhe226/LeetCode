class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort(reverse = True)
        res = []
        cur = []
        n = len(candidates)
        def dfs(i, total):
            if total == target:
                res.append(cur.copy())
                return
            if i >= n or total > target:
                return
            
            prev = -1
            for idx in range(i, n):
                if candidates[idx] == prev:
                    continue
                cur.append(candidates[idx])
                dfs(idx + 1, total + candidates[idx])
                cur.pop()
                prev = candidates[idx]
        dfs(0, 0)
        return res
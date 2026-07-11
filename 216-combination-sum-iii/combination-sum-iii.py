class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        L = 9
        res = []
        cur = []
        def dfs(i, target):
            if len(cur) == k and target == 0:
                res.append(cur[:])
                return
            if len(cur) > k or target < 0:
                return
            
            for idx in range(i, L+1):
                cur.append(idx)
                dfs(idx+1, target - idx)
                cur.pop()
        dfs(1, n)
        return res


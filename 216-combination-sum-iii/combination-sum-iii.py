class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        res = []
        cur = []
        def dfs(i, target):
            if len(cur) == k and target == 0:
                res.append(cur[:])
                return
            if len(cur) > k or target < 0:
                return
            
            for idx in range(i+1, 10):
                cur.append(idx)
                dfs(idx, target - idx)
                cur.pop()
        dfs(0, n)
        return res


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        cur = []

        n = len(nums)
        vis = [False] * n
        def dfs():
            found = False
            for i in range(n):
                if not vis[i]:
                    found = True
                    vis[i] = True
                    cur.append(nums[i])
                    dfs()
                    vis[i] = False
                    cur.pop()
            if not found:
                res.append(cur.copy())
        dfs()
        return res
        

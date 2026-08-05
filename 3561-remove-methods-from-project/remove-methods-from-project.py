class Solution:
    def remainingMethods(self, n: int, k: int, invocations: List[List[int]]) -> List[int]:
        child = [[] for i in range(n)]
        for a, b in invocations:
            child[a].append(b)

        sus = set()
        def dfs(x):
            sus.add(x)
            for i in child[x]:
                if i not in sus:
                    dfs(i)
        dfs(k)

        res = []
        for i in range(n):
            if i in sus:
                continue
            for x in child[i]:
                if x in sus:
                    return [i for i in range(n)]
            res.append(i)
        return res
        
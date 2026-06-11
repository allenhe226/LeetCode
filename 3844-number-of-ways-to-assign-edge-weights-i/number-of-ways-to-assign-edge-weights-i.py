class Solution:
    def assignEdgeWeights(self, edges: List[List[int]]) -> int:
        MOD = 10**9+7
        n = len(edges)+1
        adj = [[] for _ in range(n)]
        for x, y in edges:
            adj[x-1].append(y-1)
            adj[y-1].append(x-1)

        queue = collections.deque([(0,0)])
        maxdepth = 0
        vis = {0}
        while queue:
            node, depth = queue.popleft()
            for other in adj[node]:
                if other not in vis:
                    queue.append((other, depth+1))
                    maxdepth = max(maxdepth, depth+1)
                    vis.add(other)
        return pow(2, maxdepth-1) % MOD
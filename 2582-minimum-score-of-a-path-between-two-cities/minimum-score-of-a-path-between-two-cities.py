import collections
class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        adj = [[] for i in range(n)]
        for a, b, dist in roads:
            adj[a-1].append((b-1, dist))
            adj[b-1].append((a-1, dist))
        q = collections.deque([0])
        vis = set()
        minRoad = float("inf")
        while q:
            node = q.popleft()
            if node in vis:
                continue
            vis.add(node)
            for neighbor, dist in adj[node]:
                if neighbor not in vis:
                    q.append(neighbor)
                    minRoad = min(minRoad, dist)
        return minRoad
            


        
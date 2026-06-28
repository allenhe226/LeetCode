import heapq
class Solution:
    def minTimeMaxPower(self, n: int, edges: List[List[int]], power: int, cost: List[int], source: int, target: int) -> List[int]:
        adj = [[] for _ in range(n)]
        for u, v, t in edges:
            adj[u].append((v, t))
        q = [(0, -power, source)]
        dist = [[float("inf")] * (power+1) for i in range(n)]
        dist[source][power] = 0
        while q:
            t, p, node = heapq.heappop(q)
            if node == target:
                return [t, -p]
            if -p < cost[node]:
                continue
            p += cost[node]
            for neighbor, time in adj[node]:
                if t+time < dist[neighbor][-p]:
                    dist[neighbor][-p] = t+time
                    heapq.heappush(q, (t+time, p, neighbor))  
        return [-1,-1]
            
        
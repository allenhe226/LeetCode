from collections import deque
class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        n = len(arr)
        adj = [[] for _ in range(n)]
        for i in range(n):
            if arr[i] == 0:
                continue
            if i - arr[i] >= 0:
                adj[i].append(i-arr[i])
            if i + arr[i] < n:
                adj[i].append(i+arr[i])

        
        q = deque([start])
        vis = {start}
        while q:
            idx = q.popleft()
            if arr[idx] == 0:
                return True
            for i in adj[idx]:
                if i not in vis:
                    vis.add(i)
                    q.append(i)
        return False
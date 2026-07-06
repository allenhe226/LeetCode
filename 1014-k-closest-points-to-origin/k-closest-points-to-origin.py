class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        for i, [x,y] in enumerate(points):
            points[i] = [math.sqrt(x**2 + y**2), x, y]
        heapq.heapify(points)
        
        res = []
        for i in range(k):
            _, x, y = heapq.heappop(points)
            res.append([x,y])
        return res
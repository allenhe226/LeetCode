class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        for point in points:
            point.append(math.sqrt(point[0]**2 + point[1]**2))
        points.sort(key = lambda x : x[2])
        
        res = []
        for i in range(k):
            res.append([points[i][0], points[i][1]])
        return res
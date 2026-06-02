class Solution:
    def earliestFinishTime(self, landStartTime: List[int], landDuration: List[int], waterStartTime: List[int], waterDuration: List[int]) -> int:
        m, n = len(landStartTime), len(waterStartTime)
        landMin = min(landStartTime[i] + landDuration[i] for i in range(m))
        waterMin = min(waterStartTime[i] + waterDuration[i] for i in range(n))
        res = float("inf")
        for i in range(m):
            res = min(res, waterMin + landDuration[i]) if landStartTime[i] <= waterMin else min(res, landStartTime[i] + landDuration[i])
        for i in range(n):
            res = min(res, landMin + waterDuration[i]) if waterStartTime[i] <= landMin else min(res, waterStartTime[i] + waterDuration[i])
        return res

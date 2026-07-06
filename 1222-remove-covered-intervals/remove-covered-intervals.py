class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key = lambda x : (x[0], -x[1]))
        n = len(intervals)
        valid = [True] * n
        count = 0
        for i in range(n):
            if not valid[i]:
                continue
            start, end = intervals[i]
            for j in range(i+1,n):
                if start <= intervals[j][0] and end >= intervals[j][1]:
                    valid[j] = False
            count += 1
        return count
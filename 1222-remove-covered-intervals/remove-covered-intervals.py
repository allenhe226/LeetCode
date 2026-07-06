class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key = lambda x : (x[0], -x[1]))
        prev = (intervals[0])
        count = len(intervals)
        for i in range(1, len(intervals)):
            start, end = intervals[i]
            if prev[0] <= start and end <= prev[1]:
                count -= 1
            else:
                prev = (intervals[i])
        return count
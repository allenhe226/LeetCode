class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        res = []
        intervals = sorted(intervals, key = lambda x: x[0])
        mergestart, mergeend = intervals[0]
        for i in range(1,len(intervals)):
            start, end = intervals[i]
            if start <= mergeend:
                mergeend = max(mergeend, end)
            else:
                res.append([mergestart,mergeend])
                mergestart, mergeend = start, end
        res.append([mergestart,mergeend])
        return res
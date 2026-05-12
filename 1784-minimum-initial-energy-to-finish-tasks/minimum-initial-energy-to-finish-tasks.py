class Solution:
    def minimumEffort(self, tasks: List[List[int]]) -> int:
        n = len(tasks)
        for i in range(n):
            tasks[i].append(tasks[i][1]-tasks[i][0])
        tasks = sorted(tasks, key = lambda x : (-x[2], -x[1]))
        
        energy, cur = 0, 0
        for i in range(n):
            if tasks[i][1] - cur > 0:
                energy += tasks[i][1] - cur
                cur = tasks[i][2]
            else:
                cur = cur - tasks[i][0]
        return energy
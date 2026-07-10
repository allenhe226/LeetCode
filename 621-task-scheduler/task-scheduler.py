class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        m = len(tasks)
        letters = defaultdict(int)
        for i in range(m):
            letters[tasks[i]] += 1

        time = 1
        maxHeap = []
        queue = collections.deque([])
        for key in letters:
            heapq.heappush(maxHeap, -letters[key])
        
        while maxHeap or queue:
            if maxHeap:
                count = heapq.heappop(maxHeap)
                if count + 1 < 0:
                    queue.append((count+1, time+n+1))
                time += 1
                if queue and queue[0][1] <= time:
                    heapq.heappush(maxHeap, queue.popleft()[0])
            else:
                time = queue[0][1]
                heapq.heappush(maxHeap, queue.popleft()[0])
        return time-1
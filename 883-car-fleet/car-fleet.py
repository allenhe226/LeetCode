class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        n = len(position)
        time = []
        for i in range(n):
            time.append((target-position[i])/speed[i])

        posTime = [[position[i], time[i]] for i in range(n)]
        posTime = sorted(posTime, key=lambda x:-x[0])
        time = [posTime[i][1] for i in range(n)]

        count = 0
        stack = []
        for t in time:
            while stack and t > stack[-1]:
                stack.pop()
            if not stack:
                count += 1
            stack.append(t)
        return count
        
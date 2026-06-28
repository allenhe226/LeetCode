class Solution:
    def minLights(self, lights: list[int]) -> int:
        n = len(lights)
        diff = [0] * (n+1)
        for i in range(n):
            if lights[i] > 0:
                diff[max(0, i-lights[i])] += 1
                diff[min(n, i+lights[i]+1)] -= 1
        print(diff)
        count = cur = i = 0
        while i < n:
            cur += diff[i]
            if cur <= 0:
                count += 1
                for _ in range(2):
                    i += 1
                    if i >= n:
                        return count
                    cur += diff[i]
            i += 1
        return count


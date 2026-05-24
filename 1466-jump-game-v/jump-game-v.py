class Solution:
    def maxJumps(self, arr: List[int], d: int) -> int:
        n = len(arr)
        @functools.cache
        def getMaxJumps(i):
            result = 0
            for k in range(1,d+1):
                if i-k < 0 or arr[i-k] >= arr[i]:
                    break
                result = max(result, 1+getMaxJumps(i-k))
            for k in range(1,d+1):
                if i+k >= n or arr[i+k] >= arr[i]:
                    break
                result = max(result, 1+getMaxJumps(i+k))
            return result
        return 1+max(getMaxJumps(i) for i in range(n))
        
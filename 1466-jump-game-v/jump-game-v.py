class Solution:
    def maxJumps(self, arr: List[int], d: int) -> int:
        n = len(arr)
        vals = {}

        def findVal(i):
            if i in vals:
                return vals[i]
            choices = [1]
            for k in range(1,d+1):
                if i-k < 0 or arr[i-k] >= arr[i]:
                    break
                choices.append(1+findVal(i-k))
            for k in range(1,d+1):
                if i+k >= n or arr[i+k] >= arr[i]:
                    break
                choices.append(1+findVal(i+k))
            vals[i] = max(choices)
            return max(choices)


        maxval = 1
        for i in range(n):
            val = findVal(i)
            maxval = max(maxval,val)
        return maxval
        
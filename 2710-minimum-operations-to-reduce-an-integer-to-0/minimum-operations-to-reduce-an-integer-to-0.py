class Solution:
    def minOperations(self, n: int) -> int:
        def toBin(n):
            s = []
            while n > 0:
                s.append(n%2)
                n //= 2
            s.append(0)
            return s[::-1]
        
        def flip(arr):
            for i in range(len(arr)):
                if arr[i] == 0:
                    arr[i] = 1
                elif arr[i] == 1:
                    arr[i] = 0
            i = len(arr)-1
            while arr[i] == 1:
                arr[i] = 0
                i -= 1
            if i >= 0:
                arr[i] = 1
            return arr

        def find(arr):
            if len(arr) == 1:
                return arr[0]
            if arr[0] == 1:
                return 1 + find(arr[1:])
            if arr[0] == 0:
                return min(find(arr[1:]), 1+find(flip(arr[1:])))

        return find(toBin(n))
        
class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        n = len(arr)
        l, r = 0, n-1
        while l <= r:
            m = (l+r)//2
            if m == 0:
                l = m+1
            elif m == n-1:
                r = m-1
            elif arr[m] > arr[m-1] and arr[m] > arr[m+1]:
                return m
            elif arr[m] > arr[m-1]:
                l = m+1
            elif arr[m] < arr[m-1]:
                r = m-1
        
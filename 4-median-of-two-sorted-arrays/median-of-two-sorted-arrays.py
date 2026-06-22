class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        A, B = nums1, nums2
        n = len(A) + len(B)
        half = n // 2
        if len(B) < len(A):
            A, B = B, A
        
        l, r = 0, len(A)-1
        while True:
            i = l + (r-l)//2
            j = half - i - 2

            A_l = A[i] if i >= 0 else float("-inf")
            A_r = A[i+1] if i+1 < len(A) else float("inf")
            B_l = B[j] if j >= 0 else float("-inf")
            B_r = B[j+1] if j+1 < len(B) else float("inf")
            if A_l <= B_r and B_l <= A_r:
                if n % 2 == 0:
                    return (max(A_l, B_l) + min(A_r, B_r)) / 2.0
                else:
                    return min(A_r, B_r)
            elif A_l > B_r:
                r = i-1
            else:
                l = i+1
class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        n = len(A)
        seen = set()
        pca = [0] * n
        count = 0
        for i in range(n):
            if A[i] in seen:
                count += 1
            else:
                seen.add(A[i])
            if B[i] in seen:
                count += 1
            else:
                seen.add(B[i])
            pca[i] = count
        return pca

        
class Solution:
    def longestCommonPrefix(self, arr1: List[int], arr2: List[int]) -> int:
        prefixes = set()
        for num in arr1:
            while num > 0:
                prefixes.add(num)
                num //= 10
        res = 0
        for num in arr2:
            while num > 0 and num not in prefixes:
                num //= 10
            if num > 0:
                   res = max(res, len(str(num)))
        return res
class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        if not arr:
            return []
        n = len(arr)
        sorted_arr = sorted(arr)
        rankMap = {}
        rankMap[sorted_arr[0]] = 1
        cur = 2
        for i in range(1, n):
            if sorted_arr[i] != sorted_arr[i-1]:
                rankMap[sorted_arr[i]] = cur
                cur += 1
        for i in range(n):
            arr[i] = rankMap[arr[i]]
        return arr

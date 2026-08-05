class Solution:
    def countRatioSubarrays(self, nums: list[int], a: int, b: int) -> int:
        s = SortedList([0])
        res = pre = 0
        for x in nums:
            pre += a if x % 2 else -b
            res += s.bisect_right(pre)
            s.add(pre)
        return res
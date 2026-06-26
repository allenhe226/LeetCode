class Solution:
    def countMajoritySubarrays(self, nums: List[int], target: int) -> int:
        s = SortedList()
        s.add(0)
        cur = 0
        total = 0
        for x in nums:
            if x == target:
                cur += 1
            else:
                cur -= 1
            total += s.bisect_left(cur)
            s.add(cur)
        return total

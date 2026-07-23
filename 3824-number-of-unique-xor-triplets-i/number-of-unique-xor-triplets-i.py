class Solution:
    def uniqueXorTriplets(self, nums: List[int]) -> int:
        n = len(nums)
        if n < 3:
            return n
        if n == 3:
            return 4
        return pow(2, n.bit_length())

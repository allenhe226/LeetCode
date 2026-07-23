class Solution:
    def uniqueXorTriplets(self, nums: List[int]) -> int:
        return pow(2, len(nums).bit_length() - 1 * (len(nums) <= 2))

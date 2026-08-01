class Solution:
    def predictTheWinner(self, nums: List[int]) -> bool:
        n = len(nums)
        if ~n & 1: return True

        @cache
        def maxDiff(l, r):
            if l == r:
                return nums[l]
            return max(nums[l] - maxDiff(l+1, r), nums[r] - maxDiff(l,r-1))
        return maxDiff(0,n-1) >= 0
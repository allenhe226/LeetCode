class Solution:
    def check(self, nums: List[int]) -> bool:
        n = len(nums)
        d = False
        for i in range(n-1):
            if nums[i+1] < nums[i]:
                if not d:
                    d = True
                else:
                    return False
        if d and nums[-1] > nums[0]:
            return False
        return True

        
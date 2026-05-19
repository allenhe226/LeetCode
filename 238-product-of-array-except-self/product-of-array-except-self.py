class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)

        product = 1
        count0s = 0
        for i in range(n):
            if nums[i] == 0:
                count0s += 1
            else:
                product *= nums[i]
        
        ans = [0] * n
        if count0s > 1:
            return ans
        if count0s == 1:
            ans[nums.index(0)] = product
            return ans
        for i in range(n):
            ans[i] = product // nums[i]
        return ans
        
        
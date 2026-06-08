class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        n = len(nums)
        ans = [0] * n
        idx = 0
        for i in range(n):
            if nums[i] < pivot:
                ans[idx] = nums[i]
                idx += 1
        for i in range(n):
            if nums[i] == pivot:
                ans[idx] = nums[i]
                idx += 1
        for i in range(n):
            if nums[i] > pivot:
                ans[idx] = nums[i]
                idx += 1
        return ans
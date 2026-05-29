class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        read, write = 0, 0
        while write < n:
            if nums[write] != 0:
                temp = nums[write]
                nums[write] = nums[read]
                nums[read] = temp
                read += 1
            write += 1

        
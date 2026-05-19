class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]
        largest, smallest = [0] * n, [0] * n
        
        i = 1
        if nums[0] > 0:
            largest[0] = nums[0]
        else:
            smallest[0] = nums[0]
        while i < n:

            if nums[i] > 0:
                largest[i] = largest[i-1] * nums[i] if largest[i-1] != 0 else nums[i]
                smallest[i] = smallest[i-1] * nums[i]
            elif nums[i] < 0:
                largest[i] = smallest[i-1] * nums[i]
                smallest[i] = largest[i-1] * nums[i] if largest[i-1] != 0 else nums[i]
            i += 1
        print(largest,smallest)
        return max(largest)

            
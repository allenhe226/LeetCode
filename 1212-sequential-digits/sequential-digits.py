class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        nums = [12,23,34,45,56,67,78,89,123,234,345,456,567,678,789,1234,2345,3456,4567,5678,6789,12345,23456,34567,45678,56789,123456,234567,345678,456789,1234567,2345678,3456789,12345678,23456789,123456789]
        i, j = 0, len(nums)-1
        while i < len(nums) and nums[i] < low:
            i += 1
        while j >= 0 and nums[j] > high:
            j -= 1
        return nums[i:j+1]
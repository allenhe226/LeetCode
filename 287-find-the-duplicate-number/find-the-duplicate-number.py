class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        n = len(nums)
        slow, fast = nums[0], nums[0]
        for i in range(n):
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                slow = nums[0]
                while slow != fast:
                    slow = nums[slow]
                    fast = nums[fast]
                return fast
        return nums[0]

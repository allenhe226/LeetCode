class Solution:
    def countMajoritySubarrays(self, nums: List[int], target: int) -> int:
        count = [0]
        for num in nums:
            if num == target:
                count.append(count[-1] + 1)
            else:
                count.append(count[-1])

        ans = 0
        n = len(nums)
        for i in range(n):
            for j in range(i,n):
                if count[j+1]-count[i] > (j-i+1)//2:
                    ans += 1
        return ans

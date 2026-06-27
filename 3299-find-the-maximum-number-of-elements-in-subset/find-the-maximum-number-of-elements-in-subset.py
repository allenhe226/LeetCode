import math
class Solution:
    def maximumLength(self, nums: List[int]) -> int:
        def isPerfectSquare(x):
            i = math.isqrt(x)
            return i * i == x
        
        nums.sort()
        seen = defaultdict(int)
        length = defaultdict(int)
        ans = 1
        for num in nums:
            if isPerfectSquare(num) and seen[math.isqrt(num)] >= 2 and num != 1:
                length[num] = length[math.isqrt(num)] + 2
                print(num, length[num])
                ans = max(ans, length[num])
            else:
                length[num] = 1
            seen[num] += 1
        return max(ans, (seen[1]-1)//2 * 2 + 1)


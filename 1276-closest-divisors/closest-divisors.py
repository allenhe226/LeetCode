import math
class Solution:
    def closestDivisors(self, num: int) -> List[int]:
        for a in range(int((num+2) ** 0.5), 0, -1):
            if (num+1) % a == 0:
                return [a, (num+1)//a]
            if (num+2) % a == 0:
                return [a, (num+2)//a]
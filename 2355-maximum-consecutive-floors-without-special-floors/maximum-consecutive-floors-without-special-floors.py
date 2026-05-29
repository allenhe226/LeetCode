class Solution:
    def maxConsecutive(self, bottom: int, top: int, special: List[int]) -> int:
        floors = [bottom-1] + sorted(special) + [top+1]
        maxfloors = 0
        for i in range(len(floors)-1):
            maxfloors = max(maxfloors, floors[i+1] - floors[i] - 1)
        return maxfloors
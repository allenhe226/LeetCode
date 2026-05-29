class Solution:
    def maxConsecutive(self, bottom: int, top: int, special: List[int]) -> int:
        special.append(bottom-1)
        special.append(top+1)
        special.sort()
        maxfloors = 0
        for i in range(len(special)-1):
            maxfloors = max(maxfloors, special[i+1] - special[i] - 1)
        return maxfloors
class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        possible = set()
        for i in range(len(s)-k+1):
            possible.add(s[i:i+k])
        return len(possible) == pow(2, k)
            

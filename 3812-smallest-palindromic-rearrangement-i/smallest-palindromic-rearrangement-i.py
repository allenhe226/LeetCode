class Solution:
    def smallestPalindrome(self, s: str) -> str:
        counts = sorted(Counter(s).items())
        half = "".join(c * (k//2) for c, k in counts)
        center = "".join(c * (k%2) for c, k in counts)
        return half + center + half[::-1]
        

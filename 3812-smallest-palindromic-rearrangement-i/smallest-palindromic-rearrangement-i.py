class Solution:
    def smallestPalindrome(self, s: str) -> str:
        n = len(s)
        count = [0] * 26
        for i in range(n):
            count[ord(s[i])-97] += 1
        res = [s[n//2]] if n % 2 == 1 else []
        for i in range(25,-1,-1):
            res = [chr(i+97)] * (count[i]//2) + res + [chr(i+97)] * (count[i]//2)
        return "".join(res)
        

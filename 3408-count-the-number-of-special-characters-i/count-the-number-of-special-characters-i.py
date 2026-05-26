class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        lower = [False] * 26
        upper = [False] * 26
        for i in range(len(word)):
            if ord(word[i])-ord("a") >= 0:
                lower[ord(word[i])-ord("a")] = True
            else:
                upper[ord(word[i])-ord("A")] = True
            
        count = 0
        for i in range(26):
            if lower[i] and upper[i]:
                count += 1
        return count
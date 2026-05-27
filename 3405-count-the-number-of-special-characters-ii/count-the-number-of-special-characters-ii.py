class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        count = 0
        lower, upper = [False] * 26, [False] * 26
        for i in range(len(word)-1,-1,-1):
            val = ord(word[i])
            if val >= 97:
                lower[val-97] = True
            elif val <= 90:
                upper[val-65] = False if lower[val-65] else True
        for i in range(26):
            if lower[i] and upper[i]:
                count += 1
        return count
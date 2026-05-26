class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        count = 0
        res = [0] * 26
        lower, upper = set(), set()
        for i in range(len(word)):
            if ord(word[i]) >= ord("a") and word[i] not in lower:
                lower.add(word[i])
                val = ord(word[i])-ord("a")
                res[val] += 1
                if res[val] == 2:
                    count += 1
            elif ord(word[i]) <= ord("Z") and word[i] not in upper:
                upper.add(word[i])
                val = ord(word[i])-ord("A")
                res[val] += 1
                if res[val] == 2:
                    count += 1
        return count
class Solution:
    def processStr(self, s: str, k: int) -> str:
        length = 0
        for i in range(len(s)):
            if s[i] == "#":
                length *= 2
            elif s[i] == "*":
                if length > 0:
                    length -= 1
            elif s[i] == "%":
                continue
            else:
                length += 1

        if k > length-1:
            return "."
        for i in range(len(s)-1, -1, -1):
            if s[i] == "*":
                length += 1
            elif s[i] == "%":
                k = length-1-k
            elif s[i] == "#":
                length = length // 2
                if length != 0:
                    k = k % length
            else:
                length -= 1
                if length == k:
                    return s[i]
        return "."
        
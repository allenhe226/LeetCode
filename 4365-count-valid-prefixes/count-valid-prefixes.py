class Solution:
    def countValidPrefixes(self, s: str) -> int:
        zeros = ones = count = 0
        for i in range(len(s)):
            if s[i] == "0":
                zeros += 1
            else:
                ones += 1
            count += abs(zeros-ones) <= 1
        return count
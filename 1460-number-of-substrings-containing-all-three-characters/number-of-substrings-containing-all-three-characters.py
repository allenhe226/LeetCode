class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        last = {"a": -1, "b": -1, "c": -1}
        res = 0
        for i in range(len(s)):
            last[s[i]] = i
            res += 1 + min(last["a"], last["b"], last["c"])
        return res

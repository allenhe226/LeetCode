class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        total = 0
        n = len(s)
        count = defaultdict(int)
        l, r = 0, 0
        while r < n:
            count[s[r]] += 1
            if count["a"] and count["b"] and count["c"]:
                while count[s[l]] > 1:
                    count[s[l]] -= 1
                    l += 1
                total += l+1
            r += 1
        return total
        

class Solution:
    def distinctPoints(self, s: str, k: int) -> int:
        x, y, n = 0, 0, len(s)
        if n == k:
            return 1
        seen = set()
        dirs = {"L":(-1,0), "R":(1,0), "U":(0,1), "D":(0,-1)}
        psa = [(x,y)]
        for i in range(n):
            x, y = x + dirs[s[i]][0], y + dirs[s[i]][1]
            psa.append((x,y))
        for l in range(n-k+1):
            x = psa[-1][0] - psa[l+k][0] + psa[l][0]
            y = psa[-1][1] - psa[l+k][1] + psa[l][1]
            if (x,y) not in seen:
                seen.add((x,y))
        return len(seen)

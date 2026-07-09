class Solution:
    def sumAndMultiply(self, s: str, queries: List[List[int]]) -> List[int]:
        MOD = 10**9+7
        pow10 = [1] * 100001
        for i in range(1, 100001):
            pow10[i] = pow10[i-1] * 10 % MOD

        n = len(s)
        psa = [0] * (n+1)
        x = [0] * (n+1)
        cnt = [0] * (n+1)
        for i in range(n):
            psa[i+1] = psa[i] + int(s[i])
            x[i+1] = (x[i] * 10 + int(s[i])) % MOD if int(s[i]) > 0 else x[i]
            cnt[i+1] = cnt[i] + (int(s[i]) > 0)

        res = []
        for l, r in queries:
            length = cnt[r+1] - cnt[l]
            res.append((x[r+1] - x[l] * pow10[length]) * (psa[r+1] - psa[l]) % MOD)
        return res
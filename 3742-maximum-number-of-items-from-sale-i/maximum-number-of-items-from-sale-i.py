class Solution:
    def maximumSaleItems(self, items: List[List[int]], budget: int) -> int:
        n = len(items)
        factors = [0] * n
        for i in range(n):
            x = items[i][0]
            for j in range(n):
                if i != j and items[j][0] % x == 0:
                    factors[i] += 1
            
        dp = [float("-inf")] * (budget+1)
        dp[0] = 0
        for i in range(n):
            price = items[i][1]
            f = factors[i] + 1
            nd = dp[:]
            for j in range(price, budget+1):
                nd[j] = max(nd[j], dp[j-price] + f, nd[j-price] + 1)
            dp = nd
        return max(dp)
            
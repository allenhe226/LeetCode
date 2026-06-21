class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        maxcost = max(costs)
        count = [0] * (maxcost + 1)
        for cost in costs:
            count[cost] += 1

        res = 0
        for i in range(1, maxcost + 1):
            if coins < i:
                break
            taken = min(coins // i, count[i])
            coins -= taken * i
            res += taken
        return res
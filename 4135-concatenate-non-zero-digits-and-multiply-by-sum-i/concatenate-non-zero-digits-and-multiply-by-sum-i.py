class Solution:
    def sumAndMultiply(self, n: int) -> int:
        total = 0
        new = "0"
        for i in str(n):
            if i != "0":
                new += i
                total += int(i)
        return int(new) * total

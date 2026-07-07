class Solution:
    def sumAndMultiply(self, n: int) -> int:
        total = 0
        new = 0
        power = 0
        while n:
            if n % 10 > 0:
                new += n % 10 * pow(10, power)
                power += 1
                total += n % 10
            n //= 10
        return new * total

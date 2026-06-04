class Solution:
    def totalWaviness(self, num1: int, num2: int) -> int:
        total = 0
        for num in range(num1, num2+1):
            num = str(num)
            count = 0
            if len(num) < 3:
                continue
            for i in range(1,len(num)-1):
                n, l, r = int(num[i]), int(num[i-1]), int(num[i+1])
                if (n < l and n < r) or (n > l and n > r):
                    count += 1
            total += count
        return total
        
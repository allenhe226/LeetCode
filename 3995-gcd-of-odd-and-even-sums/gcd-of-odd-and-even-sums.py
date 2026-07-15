class Solution:
    def gcdOfOddEvenSums(self, n: int) -> int:
        def gcd(x,y):
            if y > x:
                return gcd(y, x)
            if y == 0:
                return x
            return gcd(y, x%y)

        sumOdd = sum([i for i in range(1,n*2+1,2)])
        sumEven = sum([i for i in range(0,n*2+1,2)])
        print(sumOdd, sumEven)
        return gcd(sumEven, sumOdd)
import heapq
class Solution:
    def maxNumberOfFamilies(self, n: int, reservedSeats: List[List[int]]) -> int:
        total = n * 2
        check = defaultdict(lambda: [True, True, True])
        for seat in reservedSeats:
            r, c = seat
            if c >= 2 and c <= 5:
                check[r][0] = False
            if c >= 4 and c <= 7:
                check[r][1] = False
            if c >= 6 and c <= 9:
                check[r][2] = False
            
        for key in check:
            if check[key][0] and check[key][2]:
                continue
            elif check[key][0] or check[key][1] or check[key][2]:
                total -= 1
            else:
                total -= 2
        return total


        
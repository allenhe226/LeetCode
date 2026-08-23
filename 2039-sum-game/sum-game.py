class Solution:
    def sumGame(self, num: str) -> bool:
        n = len(num)
        diff = 0
        count = 0
        for i in range(n//2):
            if num[i] == "?":
                count += 1
            else:
                diff += int(num[i])
            
            if num[n//2+i] == "?":
                count -= 1
            else:
                diff -= int(num[n//2+i])
        
        if not diff and not count:
            return False
        diff += int(count/2) * 9
        count -= int(count/2) * 2
        return diff != 0 or count != 0
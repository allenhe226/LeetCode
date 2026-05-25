class Solution:
    def canReach(self, s: str, minJump: int, maxJump: int) -> bool:
        if s[-1] == "1":
            return False
        n = len(s)
        rightMost = 0
        idxs = collections.deque([0])
        while idxs:
            i = idxs.popleft()
            for j in range(max(rightMost, i+minJump), min(i+maxJump, n-1)+1):
                if s[j] == "0":
                    if j == n-1:
                        return True
                    idxs.append(j)
            rightMost = i+maxJump+1
        return False
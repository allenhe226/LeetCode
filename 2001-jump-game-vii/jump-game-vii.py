class Solution:
    def canReach(self, s: str, minJump: int, maxJump: int) -> bool:
        n = len(s)
        rightMost = 0
        idxs = collections.deque([0])
        while idxs:
            i = idxs.popleft()
            if i == n-1:
                return True
            for j in range(max(rightMost, i+minJump), min(i+maxJump+1, n)):
                if s[j] == "0":
                    idxs.append(j)
            rightMost = i+maxJump+1
        return False
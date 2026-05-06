class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        n = len(position)
        stack = []
        ps = [(p,s) for p,s in zip(position,speed)]
        for p, s in sorted(ps)[::-1]:
            t = (target-p)/s
            while not stack or t > stack[-1]:
                stack.append(t)
        return len(stack)
        
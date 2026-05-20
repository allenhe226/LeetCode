class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        stack = []
        for c in s:
            if not stack or c != stack[-1][0]:
                stack.append([c, 1])
            elif c == stack[-1][0]:
                stack[-1][1] += 1
            if stack[-1][1] == k:
                stack.pop()
        
        print(stack)
        res = ""
        for c, f in stack:
            res += c * f
        return res
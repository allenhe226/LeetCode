class Solution:
    def smallestSubsequence(self, s: str) -> str:
        n = len(s)
        num = [0] * 26
        for i in range(n):
            num[ord(s[i]) - 97] += 1
        
        vis = [False] * 26
        stack = []
        for i in range(n):
            idx = ord(s[i]) - 97
            if not vis[idx]:
                while stack and stack[-1] > s[i]:
                    top = ord(stack[-1]) - 97
                    if num[top] > 0:
                        vis[top] = False
                        stack.pop()
                    else:
                        break
                vis[idx] = True
                stack.append(s[i])
            num[idx] -= 1
        return "".join(stack)
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n = len(heights)
        maxArea = 0
        stack = []
        for i in range(n):
            idx = i
            while stack and heights[i] < stack[-1][1]:
                idx, height = stack.pop()
                maxArea = max(maxArea, (i-idx)*height)
            stack.append((idx, heights[i])) 
        while stack:
            idx, height = stack.pop()
            maxArea = max(maxArea, (n-idx)*height)
        return maxArea
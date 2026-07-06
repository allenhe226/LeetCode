# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        mx = root.val
        def dfs(node):
            nonlocal mx
            if not node:
                return 0
            left = dfs(node.left)
            right = dfs(node.right)
            mx = max(mx, left + right + node.val)
            return max(0, left + node.val, right + node.val)
        dfs(root)
        return mx
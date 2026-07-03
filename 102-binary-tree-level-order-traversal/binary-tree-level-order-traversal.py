# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        res = []
        cur = -1
        q = collections.deque([(root, 0)])
        while q:
            node, depth = q.popleft()
            if depth > cur:
                cur = depth
                res.append([])
            res[depth].append(node.val)

            if node.left:
                q.append((node.left, depth+1))
            if node.right:
                q.append((node.right, depth+1))
        return res
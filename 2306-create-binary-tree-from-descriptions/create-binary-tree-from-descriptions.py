# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def createBinaryTree(self, descriptions: List[List[int]]) -> Optional[TreeNode]:
        nodes = {}
        children = set()
        for parent, child, isLeft in descriptions:
            if parent in nodes:
                parent_node = nodes[parent]
            else:
                parent_node = TreeNode(parent)
                nodes[parent] = parent_node

            if child in nodes:
                child_node = nodes[child]
            else:
                child_node = TreeNode(child)
                nodes[child] = child_node
            
            if isLeft:
                parent_node.left = child_node
            else:
                parent_node.right = child_node
            children.add(child_node.val)

        for node in nodes:
            if node not in children:
                return nodes[node]
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root == None: return 0
        count = 0
        def findMaxDepth(node):
            if node == None:
                return 0
            if node.left == None and node.right == None:
                return 1
            
            return max(1 + findMaxDepth(node.left),1 + findMaxDepth(node.right))
        return findMaxDepth(root)

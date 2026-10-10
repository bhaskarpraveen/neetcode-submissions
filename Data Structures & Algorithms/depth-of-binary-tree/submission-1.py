# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root: return 0

        def maxDepth(node):
            if node==None:
                return 0
            return max(1+maxDepth(node.left),1+maxDepth(node.right))
        return maxDepth(root)
    

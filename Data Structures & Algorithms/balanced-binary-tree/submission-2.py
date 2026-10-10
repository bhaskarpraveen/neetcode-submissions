# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root: return True
        
        def checkBalanced(node):
            if not node: return [True,0]
            l = checkBalanced(node.left)
            r = checkBalanced(node.right)
            val = abs(l[1]-r[1])
            check = val<2 and (l[0] and r[0])
            return [check,1 + max(l[1],r[1])]
        return checkBalanced(root)[0]


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root: return True
        
        def checkBalanced(root):
            if not root: return [True, 0]

            left = checkBalanced(root.left)
            right = checkBalanced(root.right)

            diff = abs(left[1]-right[1])
            check = diff<2 and (left[0] and right[0])
            return [check,1+max(left[1],right[1])]
        
        return checkBalanced(root)[0]

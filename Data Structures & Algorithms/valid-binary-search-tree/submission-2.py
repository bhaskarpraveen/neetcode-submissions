# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if not root: return True

        que = deque([(root,float("-inf"),float("inf"))])
        while que:
            for i in range(len(que)):
                elem,left,right = que.popleft()
                if not (left< elem.val < right):
                    return False
                if elem.left:
                    que.append((elem.left,left,elem.val))
                if elem.right:
                    que.append((elem.right,elem.val,right))
        return True
                
                
        
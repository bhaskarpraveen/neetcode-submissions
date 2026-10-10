# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root: return []
        que = deque([root])
        res=[]
        while que:
            n = len(que)
            for i in range(n):
                elem = que.popleft()
                if i==n-1:
                    res.append(elem.val)
                if elem.left:
                    que.append(elem.left)
                if elem.right:
                    que.append(elem.right)
        return res


        
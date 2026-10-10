# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        self.res = 0
        que = deque([(root,root.val)])
        while que:
            for i in range(len(que)):

                num,max_val = que.popleft()
                if num.val>=max_val:
                    self.res+=1
                if num.left:
                    que.append((num.left,max(max_val,num.val)))
                if num.right:
                    que.append((num.right,max(max_val,num.val)))
        return self.res
                


        
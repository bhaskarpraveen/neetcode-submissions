# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# approach pre-ordal number if k done
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        
        self.num = k
        self.res = 0
        def dfs(root):
            if not root:return 
            
            left = dfs(root.left)


            self.num=self.num-1
            if self.num==0:
                self.res = root.val
                return 

            right = dfs(root.right)
            
            
        dfs(root)
        return self.res

            

        
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:

        self.d = 0

        def dfs(node):
            if not node:
                return 0
            
            maxLeft = dfs(node.left)
            maxRight = dfs(node.right)

            self.d =  max(self.d, maxLeft + maxRight)
            print(self.d)

            return(1 + max(maxLeft , maxRight))
        
        dfs(root) 
        return self.d
        
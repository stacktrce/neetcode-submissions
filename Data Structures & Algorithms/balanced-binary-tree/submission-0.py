# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        
        balanced = True

        def dfs(node):

            nonlocal balanced

            if not node:
                return True

            left_max = dfs(node.left)
            right_max = dfs(node.right)

            if (abs(left_max - right_max) > 1):
                balanced = False


            return (1 + max(left_max, right_max))
            
        
        dfs(root)
        return balanced
        
            



# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        
        res = 0


        def dfs(node):

            if not node or not p or not q:
                return None
            
            if (max(q.val , p .val) < node.val):
                return dfs(node.left)
            elif (min(q.val, p.val) > node.val):
                return dfs(node.right)
        
            else:
                return node
        
        return dfs(root)
        

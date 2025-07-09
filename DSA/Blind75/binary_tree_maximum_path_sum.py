# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    mx = float('-inf')

    def maxgain(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        lg = max(self.maxgain(root.left), 0)
        rg = max(self.maxgain(root.right), 0)
        self.mx = max(self.mx, root.val + lg + rg)

        return root.val + max(lg, rg)

    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.maxgain(root)
        return self.mx



# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def invertTree(self, r: Optional[TreeNode]) -> Optional[TreeNode]:
        if r is None:
            return None
        if r.left is None and r.right is None:
            return r
        r.left, r.right = r.right, r.left
        self.invertTree(r.left)
        self.invertTree(r.right)
        return r

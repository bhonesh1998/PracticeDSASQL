# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def same(self, x1: Optional[TreeNode], x2: Optional[TreeNode]) -> bool:
        if not x1 and not x2:
            return True
        if not x1 or not x2:
            return False
        return x1.val == x2.val and self.same(x1.left, x2.left) and self.same(x1.right, x2.right)

    def isSubtree(self, r: Optional[TreeNode], sr: Optional[TreeNode]) -> bool:
        if r is None:
            return False
        if self.same(r, sr):
            return True
        return self.isSubtree(r.left, sr) or self.isSubtree(r.right, sr)



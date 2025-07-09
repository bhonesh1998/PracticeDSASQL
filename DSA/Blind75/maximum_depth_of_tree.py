# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, r: Optional[TreeNode]) -> int:
        if r is None:
            return 0
        elif r.left is None and r.right is None:
            return 1
        return 1 + max(self.maxDepth(r.left), self.maxDepth(r.right))



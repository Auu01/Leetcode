# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        # !!!Note: A leaf is a node with no children.
        if not root:
            return 0
        # If left child is None, only consider the right child's depth
        if not root.left:
            return 1 + self.minDepth(root.right)
        # If right child is None, only consider the left child's depth
        if not root.right:
            return 1 + self.minDepth(root.left)
            # If both children exist, consider the minimum depth of the two subtrees
        return 1 + min(self.minDepth(root.left), self.minDepth(root.right))

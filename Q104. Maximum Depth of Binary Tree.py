# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        #使用递归找到左右子树的最大值
        def maxdepth(root):
            if not root:
                return 0
            return 1 + max(maxdepth(root.left), maxdepth(root.right))
        return maxdepth(root)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root == None:
            return
            # a,b=b,a
        root.left, root.right = root.right, root.left
        self.invertTree(root.left)  # 当line10 return时返回这一行
        self.invertTree(root.right)

        return root

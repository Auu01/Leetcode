# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        # 辅助函数来递归检查两个子树是否镜像对称
        def isMirror(left: Optional[TreeNode], right: Optional[TreeNode]) -> bool:
            #if not left and not right:
            if (left == None) and (right == None):
                return True
            #if not left or not right:
            if (left == None) or (right == None):
                return False
            if left.val != right.val:
                return False
            return isMirror(left.left, right.right) and isMirror(left.right, right.left)
        if root == None:
            return True
        return isMirror(root.left, root.right)

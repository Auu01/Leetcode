# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        #递归辅助函数(isMirror): 接受两个节点 left 和 right，分别表示当前比较的两个子树的根节点。
        #递归终止条件：如果两个节点都是 None，表示对应的子树位置都为空，彼此对称，因此返回 True。如果其中一个节点是 None 而另一个不是，说明一个子树在这个位置有延伸而另一个没有，不对称，因此返回 False。如果两个节点都存在但是节点值不相同，也不对称，返回 False。
        #递归比较逻辑：如果两个节点值相同，为了验证它们的子树是否也是镜像的，需要进一步递归检查：left 节点的左子树与 right 节点的右子树。left 节点的右子树与 right 节点的左子树。这样确保在每一层上，两边的子树结构和值都是对称的。
        #主函数(isSymmetric): 首先检查树的根节点 root 是否为空。如果为空，根据对称定义，空树是对称的，直接返回 True。如果根节点存在，调用 isMirror 函数，以根节点的左右子节点作为参数开始递归比较，从最顶层的左右两侧开始检查是否对称。返回 isMirror 的结果，这个结果表示整个树是否对称。
        #执行流程:从根节点开始，逐层向下检查每一对节点。每次递归调用处理一对节点和它们的子节点，逐步向下扩展到叶节点。在任何时点，如果发现不对称的情况，则整个递归链将提前结束并返回 False。如果所有递归调用都验证了对称性，最终返回 True。
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

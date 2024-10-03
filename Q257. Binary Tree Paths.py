# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        '''
        def findPath(node, current_path, path):
            if node is None:
                return []
            current_path.append(str(node.val))
            if node.left == None and node.right == None:
                path.append("->".join(current_path))
            else:
                findPath(node.left, current_path, path)
                findPath(node.right, current_path, path)
            current_path.pop()
        result = []
        findPath(root, [], result)
        return result
        '''

        result = []

        def path(node  # 5, current_path):
            current_path += str(node.val)

        # cp=1+>2
        if node.right == None and node.left == None:
            result.append(current_path)
        else:
            if
        node.left:
        path(node.left, current_path + "->")
        # cp = 1+>2
        if node.right:
            path(node.right, current_path + "->")
        # cp = 1+>2+>5

        path(root, '')
        return result





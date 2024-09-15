# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # 两种方法：第一种是创建一个队列，然后通过计算当前队列的长度，这表示当前层中的节点数。为了存储这一层的所有节点值，创建一个空列表。根据当前层的节点数，进行循环：从队列中移除（deque）一个节点。将该节点的值添加到当前层的列表中。
        #       第二种是通过函数计算出树的高度，然后使用高度作为循环条件来一层一层循环

        # 方法1:
        if not root:
            return []

        result = []
        queue = deque([root])
        while queue:
            level_size = len(queue)
            level_node = []

            for _ in range(level_size):
                # pop()是从队列右端（尾部）删除一个元素，并返回该值；popleft()则是从队列左端（头部）删除
                node = queue.popleft()
                level_node.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            result.append(level_node)

        return result


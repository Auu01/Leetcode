# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if (head == None) or (head.next == None):
            return head

        node1 = head
        node2 = head.next

        node1.next = node2.next
        node2.next = node1
        head = node2

        while (node1.next != None) and (node1.next.next != None):
            last = node1
            node1 = last.next
            node2 = node1.next

            node1.next = node2.next
            node2.next = node1

            last.next = node2

        return head

        # 确定链表不为空且两个以上的节点，否则直接返回
        # 前两个node进行互换
        # 更新head值
        # 保存last位置
        # 循环：
        # 更新node1， node2的位置
        # 互换
        # last链接node2
        # 更新last
        # node1更新
        # 判断：node1是否为空？
        # 更新node2


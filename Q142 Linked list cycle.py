# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow = head #run 1 nodes every time
        fast = head #run 2 nodes every time
        #判断链表是否存在循环，假如fast和slow相遇，则链表一定存在循环
        while fast != None and fast.next != None:
            slow = slow.next
            fast = fast.next.next
            #先走，再判断，否则一开始就相等
            if slow == fast:
                break
        #如果链表没有循环，或链表只有单个node，return null
        if fast == None or fast.next == None:
            return None
        #将一个指针指向链表起始位置（head），另一个指针依旧指向第一次相遇的node
        fast = head
        #两个指针每次各走一个单位，下次相遇点为循环起始点
        while slow != fast:
            slow = slow.next
            fast = fast.next
        return slow


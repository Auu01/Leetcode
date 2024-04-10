# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        if (head.next == None) and (n == 1):
            head = None
            return head
        else:
            count = 1
            node = head
            point = head
            num = 0
            while node.next != None:
                count += 1
                node = node.next
            remove = count - n  # 3
            if count == n:
                return head.next
            while point.next != None:
                num += 1
                if num == remove:
                    point.next = point.next.next
                    break
                point = point.next
            return head

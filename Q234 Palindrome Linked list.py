# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        slow, fast = head, head
        # Two pointer: slow and fast
        # Slow move 1 node every time, and fast move two
        # When fast move to the end of list, slow just stop at the middle
        while (fast != None) and (fast.next != None):
            slow = slow.next
            fast = fast.next.next

        address = slow.next
        while address != None:
            reverse = address
            address = address.next
            reverse.next = slow
            slow = reverse
        while slow != head:
            if slow.val != head.val:
                return False
            if head.next == slow:
                return True
            slow = slow.next
            head = head.next
        return True

        # 一个快一慢找到中间点
        # 从中间点开始往后的nodes，每一个往回指，指向前一个
        # 一个从head开始，一个从尾部开始，比较是否一致

        '''    fast, slow = head, head

        while fast is not None and fast.next is not None:
            fast = fast.next.next
            slow = slow.next

        cur = slow.next

        while cur is not None:
            next_node = cur.next
            cur.next = slow
            slow = cur
            cur = next_node

        while head is not slow:
            if head.val is not slow.val:
                return False

even
            if head.next == slow:
                return True

            head = head.next
            slow = slow.next

        return True
        '''
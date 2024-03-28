# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if (head == None) or (head.next == None):
            return head
        temp = head
        res = ListNode(temp.val)
        while (temp.next != None):
            #cread a new node
            newnode = ListNode(temp.next.val)
            #connect the nodes
            newnode.next = res
            #point the next one
            temp = temp.next
            #update the value
            res = newnode
        return res
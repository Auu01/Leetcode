# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        lenth1 = 0
        lenth2 = 0

        pointA = headA
        pointB = headB
        nodeA = headA
        nodeB = headB

        while pointA.next != None:
            lenth1 += 1
            pointA = pointA.next
        while pointB.next != None:
            lenth2 += 1
            pointB = pointB.next

        if pointA != pointB:
            return None
        else:
            n = lenth1 - lenth2
            if n > 0:
                for i in range(n):
                    nodeA = nodeA.next
            else:
                for i in range(-n):
                    nodeB = nodeB.next

            while nodeA != None and nodeB != None:
                if nodeA == nodeB:
                    return nodeA
                nodeA = nodeA.next
                nodeB = nodeB.next




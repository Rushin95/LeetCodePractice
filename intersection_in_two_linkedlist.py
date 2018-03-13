# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """


        lenA = lenB = 0

        a = headA
        b = headB

        # find the lenght of both list
        while a:
            lenA += 1
            a = a.next

        while b:
            lenB += 1
            b = b.next

        diff = abs(lenA-lenB)
        a = headA
        b = headB

        # move diff steps ahead in the longer list
        if lenA > lenB:
            for _ in range(diff):
                a = a.next
        else:
            for _ in range(diff):
                b = b.next

        while a and b:
                if a == b:
                    return a
                else:
                    a = a.next
                    b = b.next
        return None




            

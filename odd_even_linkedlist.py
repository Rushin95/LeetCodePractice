# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def oddEvenList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        dummy_odd = ListNode(-1)
        odd_head = dummy_odd
        dummy_even = ListNode(-1)
        even_head = dummy_even

        while head:
            dummy_odd.next = head
            dummy_even.next = head.next

            dummy_odd = dummy_odd.next
            dummy_even = dummy_even.next

            if head.next:
                head = head.next.next
            else:
                head = None

        dummy_odd.next = even_head.next

        return odd_head.next 

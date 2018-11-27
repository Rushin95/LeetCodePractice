# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None:
            return head
        current = head
        while current.next:
            if current.next.val == current.val:
                new_next = current.next.next
                current.next = new_next
            else:
                current = current.next
        
        return head
            
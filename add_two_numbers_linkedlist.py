# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        new_list = ListNode(-1)
        l3 = new_list
        carry = 0
        while l1 or l2:
            curr_sum = carry
            if l1:
                curr_sum += l1.val
                l1 = l1.next
            if l2:
                curr_sum += l2.val
                l2 = l2.next
            next_value,carry = (curr_sum)%10, (curr_sum)//10
            l3.next = ListNode(next_value)
            l3 = l3.next
        if carry > 0:
            l3.next = ListNode(carry)

        return new_list.next

        

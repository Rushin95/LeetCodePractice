# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        # Do indorder traversal using stack

        stack = []

        # Go to extreme left
        while root:
            stack.append(root)
            root = root.left
        # While there are elements in the stack
        while stack:
            curr = stack.pop()
            k-=1
            if k == 0:
                return curr.val
            curr = curr.right
            # Go to extreme left of the right that is found
            while curr:
                stack.append(curr)
                curr = curr.left






        

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
        stack = []

        while root:
            stack.append(root)
            root = root.left

        while stack:
            curr = stack.pop()
            k-=1
            if k == 0:
                return curr.val
            curr = curr.right
            while curr:
                stack.append(curr)
                curr = curr.left






                

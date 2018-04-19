# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def convertBST(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        s = 0
        def helper(node):
            if node == None:
                return

            nonlocal s

            # go to extreme right
            if node.right:
                helper(node.right)

            # add current node to the sum
            s += node.val
            node.val = s

            # go to left
            if node.left:
                helper(node.left)
        helper(root)
        return root

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    ans = 1
    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        '''
        Time complexity: O(n)
        Space complexity: O(1)
        '''

        if root is None or (root.left is None and root.right is None):
            return 0

        def get_depth(node):

            if node is None: return 0
            left_depth = get_depth(node.left)
            right_depth = get_depth(node.right)

            self.ans = max(self.ans, left_depth + right_depth)

            return max(left_depth,right_depth) + 1
        get_depth(root)
        return self.ans

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sumOfLeftLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """

        # Using recursive calls

        ans = 0
        def helper(left,right):
            nonlocal ans
            if left != None:
                if left.left == None and left.right == None:
                    ans += left.val
                else:
                    helper(left.left,left.right)
            if right != None:
                helper(right.left, right.right)

        if root:
            helper(root.left,root.right)
        return ans




        

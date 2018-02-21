# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def getMinimumDifference(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        l = []
        def inorder(node):
            if node != None:
                inorder(node.left)
                l.append(node.val)
                inorder(node.right)

        inorder(root)

        min_abs_diff = min([abs(x-y) for x,y in zip(l,l[1:])])
        return min_abs_diff

        

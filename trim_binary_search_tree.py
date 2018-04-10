# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def trimBST(self, root, L, R):
        """
        :type root: TreeNode
        :type L: int
        :type R: int
        :rtype: TreeNode
        """
        if root is None:
            return None
        elif root.val < L:
            # root value is low so we need to check greater than root  nodes
            return self.trimBST(root.right,L,R)
        elif root.val > R:
            # root value is high so we need to check the lesser than root nodes
            return self.trimBST(root.left, L, R)
        else:
            # If the root value is in boundary, check both
            root.left = self.trimBST(root.left, L, R)
            root.right = self.trimBST(root.right,L,R)

            #return trimmed root
            return root
        

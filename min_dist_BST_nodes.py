# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def minDiffInBST(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        '''
        Time Complexity: O(n)
        Space Complexity: O(n)
        '''

        l = []
        def helper(root):
            if root:
                if root.left:
                    helper(root.left)
                l.append(root.val)
                if root.right:
                    helper(root.right)
        helper(root)
        print(l)
        ans = l[-1]
        for i in range (len(l)-1):
            ans = min(ans,l[i+1]-l[i])

        return ans

            

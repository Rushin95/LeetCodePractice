class Solution:
    def tree2str(self, t):
        """
        :type t: TreeNode
        :rtype: str
        """
        ans = ''
        def helper(node):
            nonlocal ans

            if node == None:
                pass
            else:
                ans += str(node.val)

                # add brackets for left if there is left or right
                if node.left or node.right:
                    ans += '('
                    helper(node.left)
                    ans += ')'
                # add brackets for right if and only if there is right
                if node.right:
                    ans += '('
                    helper(node.right)
                    ans += ')'
        helper(t)
        return ans

            

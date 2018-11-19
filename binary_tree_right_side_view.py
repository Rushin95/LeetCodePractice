
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        ans = []
        if root:
            this_level = [root]
            ans.append(root.val)
            while this_level and root:
                new_level = []
                for node in this_level:
                    if node.left:
                        new_level.append(node.left)
                    if node.right:
                        new_level.append(node.right)

                if len(new_level) > 0:
                    right_node = new_level[-1]
                    ans.append(right_node.val)
                    this_level = new_level
                else:
                    break
        return ans
            
        
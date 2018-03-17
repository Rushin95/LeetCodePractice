# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        stack = []
        ans = []
        completed = False
        current = root

        while not completed:
            # go to extreme left and keep on pushing elements in stack
            if current:
                stack.append(current)
                current = current.left
            # check if stack is empty
            elif len(stack) == 0:
                completed = True
            # if stack not empty, then pop one element
            else:
                current = stack[-1]
                del stack[-1]
                # add that curent element to ans
                ans.append(current.val)
                # check right and repeat the same steps
                current = current.right
        return ans


        

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def findMode(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        d = {}
        def traverse(node):
            if node.left:
                traverse(node.left)
            value = node.val
            d[value] = d.get(value,0) + 1
            if node.right:
                traverse(node.right)
        ans = []
        if root:
            traverse(root)
            max_value = max(0,max(d.values()))
            for k,v in d.items():
                if v == max_value:
                    ans.append(k)
        return ans







    

class Solution:
    def findTarget(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: bool
        """
        '''
        Time Complexity: O(v+e)
        Space Complexity: O(n)
        '''

        if root is None:
            return False
        bfs_nodes = [root]
        # set of traversed nodes
        traversed = set()

        # iterate through all the nodes in the list
        for node in bfs_nodes:
            # if the required value is in the list
            if k - node.val in traversed:
                return True
            else:
                traversed.add(node.val)
            # traverse left and right of the tree
            if node.left: bfs_nodes.append(node.left)
            if node.right: bfs_nodes. append(node.right)
        return False

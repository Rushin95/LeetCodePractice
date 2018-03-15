class Solution(object):
    count = 0
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        # using dictionary to represent matrix
        d = {}

        # initialize the first row to 1
        for i in range(m):
            d[(i,0)] = 1

        # initialize the first col to 1
        for j in range(n):
            d[(0,j)] = 1

        # the no of path to each cell is addition of top and left cell
        for i in range(1,m):
            for j in range(1,n):
                d[(i,j)] = d[(i-1,j)] + d[(i,j-1)]
        return d[(m-1,n-1)]

class Solution(object):
    def isToeplitzMatrix(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: bool
        """
        '''
        Time complexity: O(n)
        Space complexity: O(1)
        '''

        row = len(matrix)
        col = len(matrix[0])

        for r in range(row):
            for c in range(col):
                if r != 0 and c != 0:
                    if matrix[r][c] != matrix[r-1][c-1]:
                        return False
        return True

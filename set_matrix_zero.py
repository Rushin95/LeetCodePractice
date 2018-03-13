class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        row = [1]*len(matrix)
        col = [1]*len(matrix[0])

        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    row[i] = 0
                    col[j] = 0


        # making rows zoro
        for i in range(len(matrix)):
            if row[i] == 0:
                for j in range(len(matrix[0])):
                    matrix[i][j] = 0


        # making cols zero
        for j in range(len(matrix[0])):
            if col[j] == 0:
                for i in range(len(matrix)):
                    matrix[i][j] = 0

                    

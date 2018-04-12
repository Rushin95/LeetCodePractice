class Solution(object):
    def matrixReshape(self, nums, r, c):
        """
        :type nums: List[List[int]]
        :type r: int
        :type c: int
        :rtype: List[List[int]]
        """
        '''
        Time Complexity: O(n)
        Space Complexity: O(1)
        '''
        row_len = len(nums)
        col_len = len(nums[0])
        if r*c != row_len*col_len:
            return nums
        matrix = [[0]*c for _ in range(r)]
        m,n = 0,0

        for i in range(row_len):
            for j in range(col_len):
                matrix[m][n] = nums[i][j]
                n+=1
                if n == c:
                    m += 1
                    n = 0
        return matrix


            

class Solution:
    def repeatedStringMatch(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: int
        """
        '''
        Time Complexity: O(n)
        Space Complexity: O(1)
        '''

        n = 1
        while B not in A*n:
            if len(A*n) > 2*len(B):
                return -1
            else:
                n += 1
        return n



        

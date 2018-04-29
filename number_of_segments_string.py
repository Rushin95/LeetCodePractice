class Solution:
    def countSegments(self, s):
        """
        :type s: str
        :rtype: int
        """

        '''
        Time complexity: O(n)
        Space complexity: O(1)
        '''

        i = 0
        n = 0

        while i < len(s):
            # while spaces move forward
            while i < len(s) and s[i] == ' ':
                i += 1

            # increase word count if not out of bound
            if -1 < i < len(s):
                n += 1
            else:
                break

            # while word move forward
            while i < len(s) and s[i] != ' ':
                i += 1
        return n
        

class Solution(object):
    def checkRecord(self, s):
        """
        :type s: str
        :rtype: bool
        """
        '''
        Time Complexity: O(n)
        Space Complexity: O(1)

        '''

        return 'LLL' not in s and s.count('A') < 2

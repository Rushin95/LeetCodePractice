class Solution(object):
    def repeatedSubstringPattern(self, s):
        """
        :type s: str
        :rtype: bool
        """
        '''
        Time Complexity: O(n)
        Space Complexity: O(1)
        '''

        # Remove the first and last character from the new formed string anf check
        return s in (s + s)[1:-1]


            

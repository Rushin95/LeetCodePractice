class Solution:
    def validPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        '''
        Time complexity: O(n)
        Space Complexity: O(1)
        '''

        i = 0
        while i <= len(s)/2 and s[i] == s[-(i+1)]:
            i += 1

        if i == len(s):
            return True
        else:
            if i != 0:
                s = s[i:-i]
        return s[1:] == s[1:][::-1] or s[:-1] == s[:-1][::-1]


         

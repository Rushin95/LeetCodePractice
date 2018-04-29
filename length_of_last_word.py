class Solution:
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        '''
        Time complexity: O(n)
        Space complexity: O(1)
        '''


        if len(s) == 0:
            return 0

        i = len(s)-1
        n = 0
        word_found = False


        while i >= 0:
            if s[i] == ' ':
                if word_found:
                    break
                else:
                    i -= 1
            else:
                word_found = True
                n += 1
                i -= 1
        return n

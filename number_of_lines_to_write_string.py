class Solution(object):
    def numberOfLines(self, widths, S):
        """
        :type widths: List[int]
        :type S: str
        :rtype: List[int]
        """
        '''
        Time complexity: O(n)
        Space complexity: O(1)
        '''

        lines = 1
        width_sum = 0
        for letter in S:
            letter_width = widths[ord(letter)- ord('a')]
            if width_sum + letter_width  <= 100:
                width_sum += letter_width
            else:
                lines += 1
                width_sum = letter_width
        return ([lines, width_sum])

            

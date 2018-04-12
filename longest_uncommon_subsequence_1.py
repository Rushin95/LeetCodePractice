class Solution(object):
    def findLUSlength(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: int
        """
        '''
        Time Complexity: O(n)
        Space Complexity; O(1)
        '''

        # if they are same return -1
        if a == b:
            return -1
        else:
            # the one with more length would be uncommon to the smaller one
            return max(len(a),len(b))
            

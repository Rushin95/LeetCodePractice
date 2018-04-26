class Solution(object):
    def isOneBitCharacter(self, bits):
        """
        :type bits: List[int]
        :rtype: bool
        """

        '''
        Time Complexity: O(n)
        Space Complexity: O(1)
        '''

        i = 0
        flag = True
        while i < len(bits):
            if bits[i] == 1 and (bits[i+1] == 1 or bits[i+1] == 0):
                i += 2
                flag = False
            elif bits[i] == 0:
                i += 1
                flag = True
        return flag
                

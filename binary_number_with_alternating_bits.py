class Solution(object):
    def hasAlternatingBits(self, n):
        """
        :type n: int
        :rtype: bool
        """
        binary = '{0:b}'.format(n)
        for i in range(0,len(binary)-1):
            if binary[i] == binary[i+1]:
                return False
        return True

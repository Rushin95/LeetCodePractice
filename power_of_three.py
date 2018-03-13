class Solution(object):
    def isPowerOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n>0:
            # highest power of 3 => 3^19 = 1162261467
            if 1162261467 % n == 0:
                return True
        return False
        

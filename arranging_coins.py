class Solution:
    def arrangeCoins(self, n):
        """
        :type n: int
        :rtype: int
        """
        i = 0
        while n > -1:
            if n < i:
                i -= 1
                return i
            else:
                n -= i
            i += 1
        

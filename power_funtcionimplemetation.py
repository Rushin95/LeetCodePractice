class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        if n == 0:
            return 1
        elif n > 0: # if positive
            val = self.myPow(x,n/2)
            if n % 2 == 0: # n is even
                return val* val
            else: # n is odd
                return x * val*val
        else: # if negative
            val = self.myPow(x,abs(n)/2)
            if abs(n) % 2 == 0:
                return 1/(val* val)
            else:
                return 1/(x * val*val)

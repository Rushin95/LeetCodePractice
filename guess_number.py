# The guess API is already defined for you.
# @param num, your guess
# @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
# def guess(num):

class Solution(object):
    def guessNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        if guess(n) == 0 :
            return n
        start = 1
        while True:
            if guess((start + n)/2) == -1:
                n = (start+n)/2
            elif guess((start + n)/2) == 1:
                start = (start+n)/2
            elif guess((start + n)/2) == 0:
                break
        return (start+n)/2

        

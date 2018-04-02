class Solution(object):
    def rotateString(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: bool
        """

        if len(A) == len(B):
            return B in A+A
        else:
            return False

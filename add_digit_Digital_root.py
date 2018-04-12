class Solution(object):
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        # This is called Digital Root using Congruence formula
        return (num-1)%9 +1 if num != 0 else 0

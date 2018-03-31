class Solution(object):
    def findComplement(self, num):
        """
        :type num: int
        :rtype: int
        """
        # finding the 1s compliment
        # return (int('0b'+''.join(['0' if num == '1' else '1' for num in '{0:b}'.format(num)]),2))

        n = len(bin(num))-2
        return 2**n - 1 - num

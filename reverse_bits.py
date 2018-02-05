class Solution:
    # @param n, an integer(32 bit integer)
    # @return an integer
    def reverseBits(self, n):
        bin_format = ("{0:b}".format(n)).zfill(32)
        return int('0b'+ bin_format[::-1], 2)

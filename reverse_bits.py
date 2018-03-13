class Solution:
    # @param n, an integer(32 bit integer)
    # @return an integer
    def reverseBits(self, n):
        bin_format = ("{0:b}".format(n)).zfill(32)
        return int('0b'+ bin_format[::-1], 2)

    def reverseBits2(self, n):
        n_binary = bin(n)
        reverse_binary = n_binary[:2] + n_binary[2:].zfill(32)[::-1]
        return int(reverse_binary, 2)

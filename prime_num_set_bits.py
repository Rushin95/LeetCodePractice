class Solution(object):
    def countPrimeSetBits(self, L, R):
        """
        :type L: int
        :type R: int
        :rtype: int
        """
        '''
        Time complexity = O(n)
        Space complexity = O(1)
        '''


        # Maximum number of 1s in binary form of 10^6 is 20
        # List all the primes till 20
        primes = [2, 3, 5, 7, 11, 13, 17, 19]
        res = 0
        for num in range(L,R+1):
            res+= 1 if bin(num).count('1') in primes else 0
        return res

class Solution:
    def rotatedDigits(self, N):
        """
        :type N: int
        :rtype: int
        """
        '''
        Time Complexity: O(n)
        Space Complexity: O(n)
        '''

        ans = 0
        for n in range(1, N+1):
            num = str(n)
            if '3' in num or '4' in num or '7' in num:
                continue
            if '2' in num or '5' in num or '6' in num or '9' in num:
                ans += 1
        return ans

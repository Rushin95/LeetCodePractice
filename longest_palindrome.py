class Solution:
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        '''
        Time complexity: O(n)
        Space complexity: O(n)
        '''


        d = {}

        for char in s:
            d[char] = d.get(char,0) + 1

        ans = 0
        odd_found = False
        sorted_count = sorted(d.values())

        for value in sorted_count[::-1]:
            if value % 2 == 0:
                ans += value
            else:
                if not odd_found:
                    ans += value
                    odd_found = True
                else:
                    ans += value-1
        return ans

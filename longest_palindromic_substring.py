'''
Time Complexity: O(n^2)
Space Complexity: O(1)
'''

class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        # lenght of LPS for every letter would be 1 minimum
        max_length = 1
        idx = 0

        # iterate through all elements taking each as center
        for i in range(len(s)):

            # Considering the length of palidrome is Even
            a = i-1
            b = i
            even_max = 0
            # Moving away from the center
            while a >= 0 and b < len(s) and s[a] == s[b]:
                # Only change the max_length if a greater palindrome is found
                if b - a + 1 > max_length:
                    idx = a
                    max_length = b - a + 1
                a-=1
                b+=1

            # Considering the length of palidrome is Odd
            a = i - 1
            b = i + 1
            # Moving away from center
            while a >= 0 and b < len(s) and s[a] == s[b]:
                # Only change the max_length if a greater palindrome is found
                if b - a + 1 > max_length:
                    idx = a
                    max_length = b - a + 1
                a-=1
                b+=1

        return s[idx:idx+max_length]

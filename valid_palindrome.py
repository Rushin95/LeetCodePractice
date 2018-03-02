class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s = [ch.lower() for ch in s if ch.isalnum()]
        n = len(s)
        if n % 2 == 0:
            return s[:n/2] == s[n:(n/2)-1:-1]
        else:
            return s[:n/2] == s[n:(n/2):-1]
        

class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        d = {}

        for letter in s:
            d[letter] = d.get(letter,0)+1

        for i in range(len(s)):
            if d[s[i]]== 1: return i

        return -1
        

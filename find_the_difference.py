class Solution(object):
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        ans = list(t)
        for letter in s:
            ans.remove(letter)
        return ans[0]
        

class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        ans = False
        if s == t:
            ans = True
        idx1 = 0
        for idx2 in range(len(t)):
            if idx1 != len(s):
                if s[idx1] == t[idx2]:
                    idx1 += 1
                else:
                    pass
            else:
                ans = True
                break
        if idx1 == len(s):
            ans = True
        return ans

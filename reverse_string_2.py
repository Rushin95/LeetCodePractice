class Solution(object):
    def reverseStr(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        '''
        Time Complexity: O(n)
        Space Complexity: O(n)
        '''

        s = list (s)
        i = 0
        while i < len(s):
            left = len(s) - i
            if left >= 2*k:
                s[i:i+k] = reversed(s[i:i+k])
                i += 2*k
            elif left < 2*k and left >= k:
                s[i:i+k] = reversed(s[i:i+k])
                break
            elif left < k:
                s[i:] = reversed(s[i:])
                break

        return ''.join(s)

class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """

        """
        Time Complexity : O(n)
        Space Complexity : O(n)
        """

        start = 0
        max_len = 0
        d = {}

        for i in range(len(s)):

            # Check if element has occured previous
            # If it repeating start after the element's previous occurance
            if s[i] in d and d[s[i]] >= start:
                start = d[s[i]] + 1

            # Set the new occurance index for that element
            d[s[i]] = i

            max_len = max(max_len, i - start + 1)
        return max_len

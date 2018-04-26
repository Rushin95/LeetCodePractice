class Solution(object):
    def mostCommonWord(self, paragraph, banned):
        """
        :type paragraph: str
        :type banned: List[str]
        :rtype: str
        """
        '''
        Time complexity: O(n)
        Space complexity: O(n)
        '''

        # Find the ten most common words in Hamlet
        import re
        from collections import Counter
        words = re.findall(r'\w+', paragraph.lower())
        banned = set(banned)
        words = [ word for word in words if word not in banned]
        return Counter(words).most_common(1)[0][0]

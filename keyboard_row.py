import re
class Solution(object):
    def findWords(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        ans = []

        for word in words:
            if bool(re.match(r'^[qwertyuiop]*$', word,re.IGNORECASE)) or bool(re.match(r'^[asdfghjkl]*$', word,re.IGNORECASE)) or bool(re.match(r'^[zxcvbnm]*$', word,re.IGNORECASE)):
                ans.append(word)


        return ans

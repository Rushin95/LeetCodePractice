class Solution(object):
    def uniqueMorseRepresentations(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        '''
        Time Complexity : O(n^2)
        Space Complexity: O(n)
        '''

        morse_codes = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]

        ans_set = set()

        for word in words:
            transformation = ''
            for letter in word:
                transformation += morse_codes[ord(letter) - ord('a')]
            ans_set.add(transformation)

        return len(ans_set)

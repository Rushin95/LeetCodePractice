class Solution(object):
    def detectCapitalUse(self, word):
        """
        :type word: str
        :rtype: bool
        """
        '''
        Time Complexity: O(n)
        Space Complexity: O(1)
        '''


        if len(word) == 1:
            return True

        is_first_cap = word[0].isupper()
        is_second_cap = word[1].isupper()

        if is_first_cap and is_second_cap:
            for char in word:
                if char.islower():
                    return False
        elif is_first_cap and not is_second_cap:
            for char in word[1:]:
                if char.isupper():
                    return False
        elif not is_first_cap and is_second_cap:
            return False
        elif not is_first_cap and not is_second_cap:
            for char in word[2:]:
                if char.isupper():
                    return False

        return True

class Solution(object):
    def letterCasePermutation(self, S):
        """
        :type S: str
        :rtype: List[str]
        """
        '''
        Time Complexity: O(n^2)
        Space Complexity O(n)
        '''


        ans = ['']
        for char in str(S):
            if char.isdigit():
                for i in range(len(ans)):
                    ans[i] += char
            else:
                ans.extend(ans)
                for i in range(0,len(ans)/2):
                    ans[i] += char.upper()
                for i in range(len(ans)/2,len(ans)):
                    ans[i] += char.lower()

        return ans

    

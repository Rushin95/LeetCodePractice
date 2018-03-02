class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        # ce(' ','')
#         t = t.replace(' ','')

#         if len(s) != len(t):
#             return False


#         alphabets = 'abcdefghijklmnopqrstuvwxyz'
#         d1 = dict.fromkeys(list(alphabets),0)
#         d2 = dict.fromkeys(list(alphabets),0)

#         for i in range(len(s)):
#             d1[s[i]]+=1
#             d2[t[i]]+=1
#         return d1 == d2

        if len(s) != len(t):
            return False
        d1 = {}
        d2 = {}

        for letter in s:
            d1[letter] = d1.get(letter,0)+1

        for letter in t:
            d2[letter] = d2.get(letter,0)+1

        print(d1,d2)
        return d1==d2




        

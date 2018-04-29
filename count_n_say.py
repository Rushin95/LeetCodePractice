class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        if n == 1:
            return '1'
        else:
            k = 2
            new_s = '1'
            while k <= n:
                i = 0
                count = 0
                s = new_s
                new_s = ''
                print(s)
                current = s[0]
                while i < len(s):
                    if current == s[i]:
                        count += 1
                    else:
                        new_s += str(count) + current
                        current = s[i]
                        count = 1
                    i += 1
                    if i == len(s):
                        new_s += str(count) + current
                        break
                k+=1
        return new_s
            

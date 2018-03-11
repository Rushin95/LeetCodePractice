class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = [0]
        for i in s:
            if i in ['{','[','(']:
                stack.append(i)
            elif (i == '}' and stack[-1] != '{') or (i == ')' and stack[-1] != '(') or (i == ']' and stack[-1] != '['):
                return False
            else:
                stack.pop()
        return len(stack) == 1
         

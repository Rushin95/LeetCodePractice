class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        carry = 1
        for i in range(len(digits)-1,-1,-1):
            carry, digits[i] = divmod((carry+digits[i]),10)
        if carry>0:
            return [1] + digits
        return digits


        

'''
Time commplexity: greater than n
Space Complexity: n

'''

class Solution(object):
    def selfDividingNumbers(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: List[int]
        """

        ans = []
        if right == left:
            return ans

        for num in range(left,right+1):
            if '0' in str(num):
                continue
            else:
                true=[]
                for digit in str(num):
                    true.append(float(num)%int(digit) == 0)
                if all(true):
                    ans.append(num)
        return ans

class Solution(object):
    def calPoints(self, ops):
        """
        :type ops: List[str]
        :rtype: int
        """

        '''
        Time complexity: O(n)
        Space complexity: O(n)
        '''

        res = []
        for op in ops:
            if op == 'D':
                res.append(res[-1]*2)
            elif op == 'C':
                del res[-1]
            elif op == '+':
                res.append(res[-1]+res[-2])
            else:
                res.append(int(op))
        return sum(res)
                

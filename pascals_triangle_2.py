class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        res = [1]
        for _ in range(rowIndex):
            a1 = [0] + res
            a2 = res + [0]
            res = [x+y for x,y in zip(a1,a2)]
        return res

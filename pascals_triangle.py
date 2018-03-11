class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """

        def helper(n,a):
            if n == 0:
                return None
            else:
                a_next = []
                a_next.append(a[0])
                for i in range(0,len(a)-1):
                    a_next.append(a[i]+a[i+1])
                a_next.append(a[-1])
            ans.append(a_next)
            return helper(n-1,a_next)

        if numRows == 0:
            return []
        elif numRows == 1:
            return [[1]]
        else:
            ans = [[1]]
            helper(numRows-1,[1])
        return ans

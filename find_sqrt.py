class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """

        if x == 0:
            return 0

        start = 1
        end = x
        ans = None

        while start <= end:
            mid = start + ((end - start)/2)
            if mid <= x/mid:
                start = mid + 1
                ans = mid
            else:
                end = mid - 1
        return ans

       

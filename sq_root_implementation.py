class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """

        if x == 0 or x == 1:
            return x

        start = 1
        end = x/2
        ans = None

        while start <= end:
            mid = start + ((end - start)/2)
            if x/mid >= mid:
                start = mid + 1
                ans = mid
            else:
                end = mid - 1
        return ans

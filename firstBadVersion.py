# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

class Solution(object):
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        if isBadVersion(1):
            return 1

        def helper(start,end):
            print(start, end)
            if end - start == 1:
                if not isBadVersion(start):
                    if isBadVersion(end):
                        return end
            mid = start + (end - start)/2

            if isBadVersion(mid):
                end = mid
            else:
                start = mid
            return helper(start,end)

        return helper(1,n)

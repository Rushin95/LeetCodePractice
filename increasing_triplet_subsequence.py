class Solution(object):
    def increasingTriplet(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        n1,n2 = sys.maxint, sys.maxint

        for num in nums:
            # assign the smaller value to n1
            if num <= n1:
                n1 = num
            # if num is bigger than n1 than check if its between n1 and n2
            elif num <= n2:
                n2 = num
            # if num is not less than n1 and n2, we found our third number
            else:
                return True
        return False

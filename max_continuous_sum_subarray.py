
#Kadane's algorithm and some condition for all negative numbers 

class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return 0
        if all(num<0 for num in nums) == True:
            return max(nums)

        max_global = max_current = 0
        for x in nums:
            max_current = max(0, max_current + x)
            max_global = max(max_global, max_current)
        return max_global

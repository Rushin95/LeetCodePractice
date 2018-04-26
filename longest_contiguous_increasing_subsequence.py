class Solution:
    def findLengthOfLCIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        '''
        Time Complexity: O(n)
        Space Complexity: O(1)
        '''


        if len(nums) == 0:
            return 0

        res = 1
        count = 1
        for i in range(1,len(nums)):
            if nums[i] > nums[i-1]:
                count += 1
                res = max(res, count)
            else:
                count = 1
        return res

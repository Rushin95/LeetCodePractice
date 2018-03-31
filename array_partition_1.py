class Solution(object):
    def arrayPairSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        s = 0

        # take the numbers which are at the odd positions.
        # they would be minimum of the odd-even pair in sorted list
        for i in range(0,len(nums),2):
            s+=nums[i]
        return s
        

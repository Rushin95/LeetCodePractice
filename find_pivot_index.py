class Solution(object):
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        '''
        Time complexity: O(n)
        Space Complexity: O(1)
        '''

        total = sum(nums)
        left = 0
        for idx,num in enumerate(nums):
            left += num
            right = total - left
            if  right == left - num:
                return idx
        return -1

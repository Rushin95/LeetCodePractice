class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """

        if nums == []:
            return None

        # take pointers for each number
        idx0 = 0
        idx2 = len(nums) - 1
        idx1 = 0

        # while 1 pointer is on left of 2 pointer
        while idx1 <= idx2:
            # if we find 2 , swap with the 2 pointer and stay at the same place
            if nums[idx1] == 2:
                nums[idx1],nums[idx2] = nums[idx2], nums[idx1]
                idx2 -= 1
            # if we find 0 swap with the zero pointer and move ahead
            elif nums[idx1] == 0:
                nums[idx1],nums[idx0] = nums[idx0], nums[idx1]
                idx0 += 1
                idx1 += 1
            # just move ahead, 1s will automatically arrange
            elif nums[idx1] == 1:
                idx1 += 1

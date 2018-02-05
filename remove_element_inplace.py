class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val:   int
        :rtype: int
        """
        count = len(nums)
        i = 0

        if count == 0:
            return 0

        while i < len(nums):
            if nums[i] == val:
                del nums[i]
                count-=1
            else:
                i+=1
        return  count

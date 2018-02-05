class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # idx = 0
        # l = len(nums)
        # while idx < len(nums) - 1:
        #     if nums[idx] == nums[idx+1]:
        #         del nums[idx+1]
        #         l -= 1
        #     else:
        #         idx+=1
        # return l


        idx = 0
        n = len(nums)
        if n == 0 or n == 1:
            return n

        for i in range(0, n-1):
            if nums[i] != nums[i+1]:
                nums[idx] = nums[i]
                idx+=1
        nums[idx] = nums[n-1]
        return idx+1

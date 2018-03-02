class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        zero_idx = -1
        i = 0
        while i < len(nums):
            if nums[i] != 0 and zero_idx != -1:
                nums[zero_idx], nums[i] = nums[i],nums[zero_idx]
                zero_idx += 1
            elif nums[i] == 0 and zero_idx == -1:
                zero_idx = i
            i+=1


                

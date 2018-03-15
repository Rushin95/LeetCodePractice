class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        available_steps = nums[0]
        idx = 1
        n = len(nums)
        while available_steps > 0 and idx < n:
            available_steps -= 1
            available_steps = max(available_steps, nums[idx])
            idx+=1
        return idx == n

       

class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        memo = {}

        def helper(idx):
            if idx in memo:
                return memo[idx]
            elif idx > (len(nums)-3):
                memo[idx] = 0
                return 0
            elif idx == (len(nums)-3):
                memo[idx] = nums[-1]
                return nums[-1]
            else:
                memo[idx] = max(nums[idx+2] + helper(idx+2), nums[idx+3] + helper(idx+3))
            return memo[idx]

        if len(nums) == 0:
            return 0
        elif len(nums) ==2 or len(nums) == 1:
            return max(nums)
        else:
            ans = max(nums[0] + helper(0), nums[1] + helper(1))
            return ans

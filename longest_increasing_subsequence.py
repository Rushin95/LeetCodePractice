class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        dp = [1]*len(nums)
        for i in range(len(nums)):
            for j in range(i):
                # if the current i value is has j value which is less
                if nums[i] > nums[j]:
                    # save max of the (current value) and the (j value + 1)
                    dp[i] = max(dp[i], dp[j] + 1)

        return max(dp) if dp else 0


        

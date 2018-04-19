class Solution:
    def findMaxAverage(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """
        if k > len(nums):
            return sum(nums) / len(nums)

        s = 0
        max_sum = k*(-10000)
        for i in range(len(nums)):
            s += nums[i]
            if i == k - 1:
                max_sum = max(max_sum, s)
            elif i >= k:
                s -= nums[i-k]
                max_sum = max(max_sum, s)
        return max_sum/k
            

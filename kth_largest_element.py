class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        # n = len(nums)
        # for i in range(n-1,n-k-1,-1):
        #     for j in range(i):
        #         if nums[i] < nums[j]:
        #             nums[i],nums[j] = nums[j],nums[i]
        # return nums[-k]

        return sorted(nums)[-k]

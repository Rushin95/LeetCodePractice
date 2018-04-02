class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        curr_max = 0
        n = 0
        for num in nums:
            if num == 1:
                n+=1
                curr_max = max(curr_max,n)
            else:
                n = 0
        return curr_max
                

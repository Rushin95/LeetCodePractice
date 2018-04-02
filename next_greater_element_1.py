class Solution(object):
    def nextGreaterElement(self, findNums, nums):
        """
        :type findNums: List[int]
        :type nums: List[int]
        :rtype: List[int]
        """
        d = {}
        for i in range(len(nums)):
            for j in range(i,len(nums)):
                if nums[j] > nums[i]:
                    d[nums[i]] = nums[j]
                    break
                if j == len(nums) - 1:
                    d[nums[i]] = -1

        return map(lambda x: d[x],findNums)

                    

class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if len(nums) == 0:
            return [[]]
        s = []
        s.append([nums[0]])
        for num in nums[1:]:
            temp = []
            for each in s:
                for i in range(len(each) + 1):
                    temp.append(each[:i] + [num] + each[i:])
            s = temp
        return s

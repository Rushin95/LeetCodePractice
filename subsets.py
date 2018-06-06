class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if len(nums) == 0:
            return [[]]
        else:
            temp = self.subsets(nums[1:])
            ans = []
            print(temp)
            for each in temp:
                print(each)
                ans.append([nums[0]] + each)
                ans.append(each)
            return ans

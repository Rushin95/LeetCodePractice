class Solution(object):
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        '''
        Time complexity: O(n)
        Space complexity: O(1)
        '''


        if len(nums) < 2:
            return 0
        else:
            is_left_small = True
            is_right_small = False

            for i in range(len(nums)):
                if i == 0 :
                    is_left_small = True
                else:
                    is_left_small = nums[i-1] < nums[i]

                if i == len(nums)-1 :
                    is_right_small = True
                else:
                    is_right_small = nums[i+1] < nums[i]

                if is_left_small and is_right_small:
                    return i

            return 1

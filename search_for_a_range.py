class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        '''
        Time complexity: O(logn)
        Space complexity: O(1)
        '''



        if len(nums) == 1 and nums[0] == target:
            return [0,0]

        left  = 0
        right = len(nums) - 1

        ans = [-1,-1]

        while left <= right:
            mid = (left+right)/2
            if target > nums[mid]:
                left = mid + 1
            elif target < nums[mid]:
                right = mid - 1
            else:
                left = mid
                right = mid
                ans = [left,right]
                while left >= 0:
                    if nums[left] != target:
                        break
                    ans[0] = left
                    left -= 1
                while right < len(nums):
                    if nums[right] != target:
                        break
                    ans[1] = right
                    right += 1
                break
        return ans

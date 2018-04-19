class Solution:
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        deque = []
        res = []

        for i in range(len(nums)):

            # if the first index is out of the k boundary, remove it
            if len(deque) != 0 and deque[0] == i - k:
                del deque[0]


            # Now deque has index of those elements which are in current window
            # If the element at the last index is smaller than the current element
            # it will never be max in any further windows. So remove it
            while  len(deque) != 0 and nums[deque[-1]] < nums[i]:
                del deque[-1]


            deque.append(i)

            # start appending to result only when the k-1 elements have passed
            if i >= k-1:
                res.append(nums[deque[0]])


        return res

                

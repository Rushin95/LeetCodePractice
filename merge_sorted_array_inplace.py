class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: void Do not return anything, modify nums1 in-place instead.
        """

        if n == 0:
            return

        idx1 = m - 1
        idx2 = n - 1
        idx3 = m+n-1

        while idx1 >= 0 and idx2 >= 0 and idx3 >= 0:
            if nums1[idx1] >= nums2[idx2]:
                nums1[idx3] = nums1[idx1]
                idx1 -= 1

            elif nums1[idx1] < nums2[idx2]:
                nums1[idx3] = nums2[idx2]
                idx2 -= 1
            idx3 -= 1

        if idx2 >= 0:
            nums1[:idx2+1] = nums2[:idx2+1]
                

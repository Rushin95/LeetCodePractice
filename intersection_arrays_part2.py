class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """

        ans = []
        if len(nums1) == 0 or len(nums2) == 0:
            return ans
        n1 = sorted(nums1)
        n2 = sorted(nums2)


        i = 0
        j = 0
        while True:
            if i == len(n1) or j == len(n2):
                break
            if n1[i] < n2[j]:
                i+=1
            elif n1[i] > n2[j]:
                j+=1
            elif n1[i] == n2[j]:
                ans.append(n1[i])
                i+=1
                j+=1

        return ans

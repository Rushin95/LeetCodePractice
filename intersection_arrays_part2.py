class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """

#         if len(nums1)==0 or len(nums2)==0:
#             return []
#         ans = []
#         d1 = {}
#         d2 = {}
#         for num in nums1:
#             d1[num] = d1.get(num,0)+1
#         for num in nums2:
#             d2[num] = d2.get(num,0)+1

#         if len(d1) < len(d2):
#             for key in d1.keys():
#                 if key in d2:
#                     ans+=([key]*min(d1[key],d2[key]))
#         else:
#             for key in d2.keys():
#                 if key in d1:
#                     ans+=([key]*min(d1[key],d2[key]))

#         return ans

        d1 = {}
        for num in nums1:
            d1[num] = d1.get(num,0)+1
        d2 = []
        for num in nums2:
            if num in d1 and d1[num] > 0:
                d2.append(num)
                d1[num] -= 1
        return d2

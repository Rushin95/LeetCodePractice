class Solution(object):
    def findPairs(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        '''
        Time Complexity: O(n)
        Space Complexity: O(n)
        '''

        if k < 0:
            return 0
        d = {}
        count = 0
        for num in nums:
            d[num] = d.get(num,0) + 1
        for key in d.keys():
            if k == 0:
                if d[key] >= 2:
                    count += 1
            else:
                if (key+k) in d:
                    count += 1

        return count

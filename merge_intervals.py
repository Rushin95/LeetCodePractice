# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        '''
        Time complexity:O(nlogn)
        Space Complexity: O(1)
        '''

        n = len(intervals)
        if n == 0: return []
        intervals = sorted(intervals, key = lambda x : x.start)
        ans = [intervals[0]]

        for i in range(1,n):
            prev = ans[-1]
            curr = intervals[i]

            if curr.start <= prev.end:
                ans[-1].end = max(prev.end, curr.end)
            else:
                ans.append(curr)
        return ans

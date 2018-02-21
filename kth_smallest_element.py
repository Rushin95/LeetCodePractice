class Solution(object):
    def kthSmallest(self, matrix, k):
        """
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int
        """
        l = []
        for row  in matrix:
            for element in row:
                l.append(element)
        return sorted(l)[k-1]

        

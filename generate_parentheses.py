class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        if n == 0:
            return []
        br = set(['()'])
        for i in range(n-1):
            temp = set()
            # for each string in set
            for st in br:
                # for each location in string
                for j in range(len(st) + 1):
                    # insert '()' at that location
                    temp.add(st[:j] + '()' + st[j:])
            br = set(temp)
        return list(br)

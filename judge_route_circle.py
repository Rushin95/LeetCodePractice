class Solution(object):
    def judgeCircle(self, moves):
        """
        :type moves: str
        :rtype: bool
        """
        d = {'U':0,
             'D':0,
             'L':0,
             'R':0}

        for move in moves:
            d[move]+=1

        if d['U'] != d['D'] or d['L'] != d['R']:
            return False
        return True

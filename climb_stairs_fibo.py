# Dynamic Programming Memoization
class Solution(object):
    memo = {}
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n in self.memo:
            return self.memo[n]
        elif n == 1 or n == 2 or n == 0:
            self.memo[n] = n
            return n
        else:
            self.memo[n] = self.climbStairs(n-1) + self.climbStairs(n-2)
            return self.memo[n]

class Solution(object):
    def minCostClimbingStairs(self, cost):
        """
        :type cost: List[int]
        :rtype: int
        """
        memo = {}
        def helper(cost, step):
            if step in memo:
                return memo[step]
            else:
                if step >= len(cost) - 2:
                    memo[step] = 0
                    return 0
                else:
                    ans = min(cost[step+1]+ helper(cost,step+1),cost[step+2]+ helper(cost,step+2))
                    memo[step] = ans
                    return ans
        return helper(cost, -1)

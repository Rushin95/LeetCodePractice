class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        ans = 0
        for i in  range(len(prices)-1):
            ans += max(prices[i+1] - prices[i], 0)
        return ans
            

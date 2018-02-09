class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if len(prices) < 2:
            return 0
        mini = prices[0]
        max_profit = 0
        for price in prices:
            max_profit = max(price - mini , max_profit)
            mini = min(mini, price)
        return max_profit

        

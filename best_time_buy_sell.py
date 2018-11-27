class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if len(prices) < 2:
            return 0
        minimum_buy_price = prices[0]
        max_profit = 0
        for price in prices:
            # compare current profit
            if price - minimum_buy_price > max_profit:
                max_profit = price - minimum_buy_price
            
            # update the minimum buying price
            if price < minimum_buy_price:
                minimum_buy_price = price
        return max_profit
                
            
                
        
        
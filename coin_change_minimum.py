class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        coins = sorted(coins)
        coin_len = len(coins)

        # create array which returns min coin required to make the index value
        min_coin_for = [amount+1]*(amount+1)
        min_coin_for[0] = 0

        for i in range(1,amount + 1):
            for j in range(coin_len):
                if coins[j] <= i:
                    # if amount is greater than or equal to denomination
                    # go up in row denomination times and add 1 to that value and check min
                    min_coin_for[i] = min(min_coin_for[i], min_coin_for[i - coins[j]] + 1 )

        if min_coin_for[amount] > amount:
            return -1
        else:
            return min_coin_for[amount]
     

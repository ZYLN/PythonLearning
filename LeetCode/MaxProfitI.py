class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        # if len(prices) < 2:
        #     return 0
        # v_min = prices[0]
        # v_max = prices[1]
        # profit = prices[1] - prices[0]
        # for i, v in enumerate(prices[1:]):
        #     if v - v_min >= profit:
        #         v_max = v
        #         profit = v_max - v_min
        #         # continue
        #     if v_min > v:
        #         v_min = v
        #         v_max = v
        # return profit if profit > 0 else 0
        min_price, max_profit = 999999, 0                #动态规划 前i天的最大收益 = max{前i-1天的最大收益，第i天的价格-前i-1天中的最小价格}
        for i in range(len(prices)):
            min_price = min(min_price, prices[i])
            max_profit = max(max_profit, prices[i] - min_price)
        return max_profit

s = Solution()
print(s.maxProfit([4,1,5]))
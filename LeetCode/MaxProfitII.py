class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        profit = 0
        for i, v in enumerate(prices[0:-1]):
            profit += prices[i + 1] - prices[i] if prices[i + 1] > prices[i] else 0
        return profit
s = Solution()
print(s.maxProfit([4,1,5]))
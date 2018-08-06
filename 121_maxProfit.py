# encoding = utf-8


class Solution:
    def maxProfit(self, prices):
        """
        calculate the maximum profit
        :param prices:List[int]
        :return:int
        """
        if len(prices) == 0:
            return 0
        max_profit = 0
        cur_min = prices[0]
        for i in prices:
            if i - cur_min > max_profit:
                max_profit = i - cur_min
            elif i - cur_min < 0:
                cur_min = i
        return max_profit


prices = []
max_profit = Solution().maxProfit(prices)
print(max_profit)
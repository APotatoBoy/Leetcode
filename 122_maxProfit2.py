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
        temp = 0
        cur_min = prices[0]
        for i in prices:
            if i - cur_min > temp or i - cur_min == temp:
                temp = i - cur_min
            else:
                #i - cur_min < temp:
                max_profit += temp
                temp = 0
                cur_min = i
        max_profit += temp
        return max_profit


prices = [7,1,5,3,6,4]
max_profit = Solution().maxProfit(prices)
print(max_profit)
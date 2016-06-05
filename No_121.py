class Solution(object):

    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if not prices:
            return 0
        max_profit = -1
        buy_price = prices[0]
        for i in range(1, len(prices)):
            cur_price = prices[i]
            cur_profit = cur_price - buy_price
            max_profit = max(max_profit, cur_profit)
            buy_price = min(buy_price, cur_price)

        return 0 if max_profit < 0 else max_profit


if __name__ == '__main__':
    my_solution = Solution()
    s = [1]
    print my_solution.maxProfit(s)
# 121. Best Time to Buy and Sell Stock
#
# You are given an array prices where prices[i] is the price of a given stock
# on the ith day.
#
# You want to maximize your profit by choosing a single day to buy one stock
# and choosing a different day in the future to sell that stock.
#
# Return the maximum profit you can achieve from this transaction. If you
# cannot achieve any profit, return 0.

from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minimum = prices[0]
        profit = 0

        for index in range(1, len(prices)):
            if prices[index] < minimum:
                minimum = prices[index]
            else:
                currentProfit = prices[index] - minimum
                if currentProfit > profit:
                    profit = currentProfit

        return profit

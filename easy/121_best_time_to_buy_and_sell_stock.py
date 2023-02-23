"""
You are given an array prices where prices[i] is the price of a given stock on the ith day.

You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.
------------------
time
O(n)

memory
O(1)
"""

from typing import List


class Solution:
    def max_profit(self, prices: List[int]) -> int:
        max_profit = 0
        min_price = float("inf")

        for i in range(len(prices)):
            if prices[i] < min_price:
                min_price = prices[i]
            elif prices[i] - min_price > max_profit:
                max_profit = prices[i] - min_price

        return max_profit


print(Solution().max_profit([7, 1, 5, 3, 6, 4]))
print(Solution().max_profit([7, 6, 4, 3, 1]))

"""
You are given an m x n integer grid accounts where accounts[i][j] is the amount of money the i​​​​​​​​​​​th​​​​ customer has in the j​​​​​​​​​​​th​​​​ bank. Return the wealth that the richest customer has.

A customer's wealth is the amount of money they have in all their bank accounts. The richest customer is the customer that has the maximum wealth.
---------------
speed
O(n)

memory
O(1)
"""

from typing import List


class Solution:
    def maximum_wealth(self, accounts: List[List[int]]) -> int:
        return max([sum(account) for account in accounts])


print(Solution().maximum_wealth([[1, 2, 3], [3, 2, 1]]))

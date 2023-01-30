"""
You are given an integer array prices where prices[i] is the price of a given stock on the ith day.

On each day, you may decide to buy and/or sell the stock. You can only hold at most one share of the stock at any time.
However, you can buy it then immediately sell it on the same day.

Find and return the maximum profit you can achieve.


Example 1:

Input: prices = [7,1,5,3,6,4]
Output: 7
Explanation: Buy on day 2 (price = 1) and sell on day 3 (price = 5), profit = 5-1 = 4.
Then buy on day 4 (price = 3) and sell on day 5 (price = 6), profit = 6-3 = 3.
Total profit is 4 + 3 = 7.

Example 2:

Input: prices = [1,2,3,4,5]
Output: 4
Explanation: Buy on day 1 (price = 1) and sell on day 5 (price = 5), profit = 5-1 = 4.
Total profit is 4.
Example 3:

Input: prices = [7,6,4,3,1]
Output: 0
Explanation: There is no way to make a positive profit, so we never buy the stock to achieve the maximum profit of 0.


Constraints:

1 <= prices.length <= 3 * 104
0 <= prices[i] <= 104
"""


# Solution 1
class Solution:
    def maxProfit(self, prices: list[int]) -> int:

        if len(prices) <= 1:
            return 0

        local_minima_maxima = []

        if prices[0] != prices[1]:
            local_minima_maxima.append(0)

        if prices[-1] != prices[-2]:
            local_minima_maxima.append(len(prices) - 1)

        for i in range(1, len(prices) - 1):

            if (prices[i - 1] > prices[i] < prices[i + 1]) or (prices[i - 1] < prices[i] > prices[i + 1]):
                local_minima_maxima.append(i)

            if (prices[i - 1] > prices[i] == prices[i + 1]) or (prices[i - 1] == prices[i] < prices[i + 1]) or (
                    prices[i - 1] < prices[i] == prices[i + 1]) or (prices[i - 1] == prices[i] > prices[i + 1]):
                local_minima_maxima.append(i)

        local_minima_maxima.sort()

        if len(local_minima_maxima) == 0:
            return 0

        if len(local_minima_maxima) == 1:
            ind = local_minima_maxima[0]

            if ind == 0:
                if prices[ind] == max(prices):
                    return 0
                else:
                    return max(0, max(prices) - prices[ind])

            else:
                if prices[ind] == max(prices):
                    return max(0, prices[ind] - min(prices))
                else:
                    return 0

        if len(local_minima_maxima) == 2:
            min_val = local_minima_maxima[0]
            max_val = local_minima_maxima[1]
            return max(0, prices[max_val] - prices[min_val])

        max_profit = 0

        for i in range(len(local_minima_maxima) - 1):
            max_profit += max(0, prices[local_minima_maxima[i + 1]] - prices[local_minima_maxima[i]])

        return max_profit


# Solution 2
class Solution:
    def maxProfit(self, prices: list[int]) -> int:

        profit = 0

        for i in range(1, len(prices)):
            if prices[i - 1] < prices[i]:
                profit += (prices[i] - prices[i - 1])

        return profit

#
# @lc app=leetcode id=121 lang=python3
#
# [121] Best Time to Buy and Sell Stock
#

# @lc code=start
class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        # Solution 1: Brute Force - Doesn't Work
        # Time Complexity: O(n^2)
        # Space Complexity: O(1)

        # profit = 0

        # for i in range (0, len(prices)):
        #     for j in range (i + 1, len(prices)):
        #         if (-prices[i] + prices[j]) > profit:
        #             profit = -prices[i] + prices[j]

        # return profit

        # Solution 2
        # Time Complexity: O(n)
        # Space Complexity: O(1)

        # Edge Case
        if not prices:
            return 0

        profit = 0
        minPrice = prices[0]

        for i in range (1, len(prices)):
            profit = max(profit, prices[i] - minPrice)
            minPrice = min(minPrice, prices[i])

        return profit
# @lc code=end


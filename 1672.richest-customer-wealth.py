#
# @lc app=leetcode id=1672 lang=python3
#
# [1672] Richest Customer Wealth
#

# @lc code=start
class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:

        # Solution 1:
        # Time Complexity: O(MN)
        # Space Complexity: O(1)

        maxSum = 0
        tempSum = 0

        for i, array in enumerate(accounts):
            for j, value in enumerate(array):
                tempSum += value

                if tempSum > maxSum:
                    maxSum = tempSum

            tempSum = 0

        return maxSum

# @lc code=end


#
# @lc app=leetcode id=1342 lang=python3
#
# [1342] Number of Steps to Reduce a Number to Zero
#

# @lc code=start
class Solution:
    def numberOfSteps(self, num: int) -> int:

        # Solution 1:
        # Time Complexity: O(logn)
        # Space Complexity: O(1)

        ret_steps = 0

        while num > 0:
            # If even, divide by 2
            if (num % 2 == 0):
                num /= 2
                ret_steps += 1
            # If odd, subtract 1
            else:
                num -= 1
                ret_steps += 1

        return ret_steps

# @lc code=end


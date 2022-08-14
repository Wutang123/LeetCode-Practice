#
# @lc app=leetcode id=70 lang=python3
#
# [70] Climbing Stairs
#

# @lc code=start
class Solution:
    def climbStairs(self, n: int) -> int:

        # Solution 1: (Fibonacci)
        # Time Complexity: O(x), where x is n - 2
        # Space Complexity: O(1)

        if n == 1:
            return 1

        elif n == 2:
            return 2

        n_1 = 1
        n_2 = 2
        count = 0
        while count < (n - 2):
            nth = n_1 + n_2
            n_1 = n_2
            n_2 = nth
            count += 1

        return nth



# @lc code=end


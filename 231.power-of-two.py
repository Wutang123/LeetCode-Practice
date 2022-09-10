#
# @lc app=leetcode id=231 lang=python3
#
# [231] Power of Two
#

# @lc code=start
class Solution:
    def isPowerOfTwo(self, n: int) -> bool:

        # Solution 1:
        # Time Complexity: O(1)
        # Space Complexity: O(1)

        # Edge Case:
        if n <= 0:
            return False

        count = 0
        for i in range(0, 32):
            if n & 1:
                count += 1

            if count > 1:
                return False

            n = n >> 1

        return True

# @lc code=end


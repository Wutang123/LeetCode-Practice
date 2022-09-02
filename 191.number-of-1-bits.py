#
# @lc app=leetcode id=191 lang=python3
#
# [191] Number of 1 Bits
#

# @lc code=start
class Solution:
    def hammingWeight(self, n: int) -> int:

        # Solution 1:
        # Time Complexity: O(n), where n is the 32
        # Space Complexity: O(1)

        count = 0

        for i in range(0, 32):
            if n & 1: # AND Gate
                count += 1

            n = n >> 1 # Bit Shift Right

        return count

# @lc code=end


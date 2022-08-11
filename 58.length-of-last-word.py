#
# @lc app=leetcode id=58 lang=python3
#
# [58] Length of Last Word
#

# @lc code=start
class Solution:
    def lengthOfLastWord(self, s: str) -> int:

        # Solution 1:
        # Time Complexity: O(n), where n is the size of the string
        # Space Complexity: O(1)

        words = s.split()
        return len(words[-1])

# @lc code=end


#
# @lc app=leetcode id=171 lang=python3
#
# [171] Excel Sheet Column Number
#

# @lc code=start
class Solution:
    def titleToNumber(self, columnTitle: str) -> int:

        # Solution 1:
        # Time Complexity: O(n), where n is the length of the str
        # Space Complexity: O(1)
        count = 0
        ret = 0
        for i in range(len(columnTitle) - 1, -1, -1):

            letter_val = ord(columnTitle[i]) - ord("A") + 1
            ret += ( letter_val * (26 ** count) )
            count += 1

        return ret

# @lc code=end


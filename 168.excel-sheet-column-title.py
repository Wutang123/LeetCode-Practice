#
# @lc app=leetcode id=168 lang=python3
#
# [168] Excel Sheet Column Title
#

# @lc code=start
class Solution:
    def convertToTitle(self, columnNumber: int) -> str:

        # Solution 1:
        # Time Complexity: O(n)
        # Space Complexity: O(1)

        ret = ""

        while columnNumber:

            columnNumber -= 1
            remainder = columnNumber % 26
            columnNumber = columnNumber // 26

            ret = chr(remainder + ord('A')) + ret

        return ret

# @lc code=end


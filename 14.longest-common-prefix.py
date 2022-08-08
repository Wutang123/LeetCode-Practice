#
# @lc app=leetcode id=14 lang=python3
#
# [14] Longest Common Prefix
#

# @lc code=start
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:

        # Solution 1:
        # Time Complexity: O(S), where is S is the of characters in the array
        # Space Complexity: O(1)

        output = ""

        for i in range(len(strs[0])):
            for string in strs:
                if ( (i == len(string)) or (string[i] != strs[0][i]) ):
                    return output
            output += strs[0][i]

        return output

# @lc code=end


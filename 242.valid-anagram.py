#
# @lc app=leetcode id=242 lang=python3
#
# [242] Valid Anagram
#

# @lc code=start
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        # Solution 1: Dictionary
        # Time Complexity: O(n), where n is the length of the strings
        # Space Complexity: O(n), where n is the length of the strings
        dict_list_s = {}
        dict_list_t = {}

        # Edge Case: (len mismatch)
        if len(s) != len(t):
            return False

        for i in range(0, len(s)):
            if s[i] in dict_list_s:
                dict_list_s[s[i]] += 1
            else:
                dict_list_s[s[i]] = 1

            if t[i] in dict_list_t:
                dict_list_t[t[i]] += 1
            else:
                dict_list_t[t[i]] = 1

        return dict_list_s == dict_list_t

# @lc code=end


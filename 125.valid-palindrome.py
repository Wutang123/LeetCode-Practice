#
# @lc app=leetcode id=125 lang=python3
#
# [125] Valid Palindrome
#

# @lc code=start
class Solution:
    def isPalindrome(self, s: str) -> bool:

        # Solution 1:
        # Time Complexity: O(n), O(n), where n is the length of s
        # Space Complexity: O(1)

        if len(s) == 1:
            return True

        i = 0
        j = len(s) - 1
        s = s.lower()

        while i < j:

            # Move the left pointer to right so it points to a alphanumeric character
            while i < j and not s[i].isalnum():
                i += 1

            # Move the right pointer to right so it points to a alphanumeric character
            while i < j and not s[j].isalnum():
                j -= 1

            if s[i] != s[j]:
                return False

            i += 1
            j -= 1

        return True

# @lc code=end


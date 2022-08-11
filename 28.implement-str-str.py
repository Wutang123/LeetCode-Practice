#
# @lc app=leetcode id=28 lang=python3
#
# [28] Implement strStr()
#

# @lc code=start
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:

        # Solution 1: (Simple)
        # Time Complexity: O(M * N), where M is the length of the substring and N is the length of the of the string
        # Space Complexity: O(1)

#         # Edge Case:
#         if not needle:
#             return 0

#         if needle in haystack:
#             return haystack.find(needle)
#         else:
#             return -1


        # Solution 2: (For loop)
        # Time Complexity: O(M * N), where M is the length of the substring and N is the length of the of the string
        # Space Complexity: O(1)

        # Edge Case:
        if not needle:
            return 0

        for i in range(0, len(haystack) - len(needle) + 1):
            for j in range(0, len(needle)):
                if needle[j] != haystack[i + j]:
                    break
                elif (j == len(needle) - 1):
                    return i

        return -1


# @lc code=end


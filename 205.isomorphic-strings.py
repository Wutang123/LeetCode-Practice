#
# @lc app=leetcode id=205 lang=python3
#
# [205] Isomorphic Strings
#

# @lc code=start
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:

        # Solution 1:
        # Time Complexity: O(n^2), where n is the length of string s
        # Space Complexity: O(n), where n is the length of string s

        # Get key from value
        # def getKey_fromValue(char_dict, val):
        #     ret = None
        #     for key, value in char_dict.items():
        #         if val == value:
        #             return key
        #     return ret

        # Check if either are empty strings
        # if (not s) or (not t):
        #     return False

        # Check if strings are both the same
        # if s == t:
        #     return True

        # char_dict = {} # Store all see characters
        # t = list(t)
        # for i in range(0, len(s)):
        #     if s[i] not in char_dict:
        #         char_dict[s[i]] = t[i]

        #     if checkValue(char_dict, t[i]):
        #         t[i] = getKey_fromValue(char_dict, t[i]) # Replace current index with corresponding key
        #     else:
        #         return False

        # t = ''.join(t)
        # if s == t:
        #     return True
        # else:
        #     return False

        #=======================================

        # Solution 2:
        # Time Complexity: O(n), where n is the length of string s
        # Space Complexity: O(n), where n is the length of string s

        # # Check if either are empty strings
        # if (not s) or (not t):
        #     return False

        # # Check if strings are both the same
        # if s == t:
        #     return True

        # char_dict = {} # Store all see characters
        # for i in range(0, len(s)):
        #     # If key doesn't exist and value doesn't exist add to dictionary
        #     if t[i] not in char_dict and s[i] not in char_dict.values():
        #         char_dict[t[i]] = s[i]

        #     # If value not in dictionary return False
        #     if t[i] not in char_dict:
        #         return False
        #     else: # Otherwise replace the current index with it
        #         t = t[:i] + char_dict[t[i]] + t[i+1:]

        # if s == t:
        #     return True
        # else:
        #     return False

        #=======================================
        # Solution 3:
        # Time Complexity: O(n), where n is the length of string s
        # Space Complexity: O(n), where n is the length of string s

        map1 = []
        map2 = []

        for char_s in s:
            map1.append(s.index(char_s))

        for char_t in t:
            map2.append(t.index(char_t))

        if map1 == map2:
            return True

        return False

# @lc code=end


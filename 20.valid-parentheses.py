#
# @lc app=leetcode id=20 lang=python3
#
# [20] Valid Parentheses
#

# @lc code=start
class Solution:
    def isValid(self, s: str) -> bool:

        # Solution 1:
        # Time Complexity: O(n), where n is the length of s
        # Space Complexity: O(1)

        fifo = []
        parenthese_dict = {
            "(" : 0  ,
            ")" : "(",
            "[" : 0  ,
            "]" : "[",
            "{" : 0  ,
            "}" : "{"
        }

        # Inital Check (Verify input array is even)
        if len(s) % 2 !=0:
            return False

        # Edge Case (Verify first character is not a closer)
        if parenthese_dict[s[0]] != 0:
            return False

        for char in s:
            fifo.append(char)

            if (len(fifo) > 1):
                if (fifo[fifo.index(char) - 1] == parenthese_dict[char]):
                    fifo.pop()
                    fifo.pop()

        return fifo == []


# @lc code=end


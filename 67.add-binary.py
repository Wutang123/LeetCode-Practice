#
# @lc app=leetcode id=67 lang=python3
#
# [67] Add Binary
#

# @lc code=start
class Solution:
    def addBinary(self, a: str, b: str) -> str:

        # Solution 1: (Binary Conversion)
        # Time Complexity: O(n), where n is the length of the string
        # Space Complexity: O(1)

        # int_a = int(a, 2)
        # int_b = int(b, 2)

        # return "{0:b}".format(int_a + int_b)

        # Solution 2: (Binary Addition)
        # Time Complexity: O(n), where n is the length of the string
        # Space Complexity: O(1)
        i = len(a) - 1
        j = len(b) - 1
        carry_bit = 0
        return_list = ""

        while i >= 0 or j >= 0:

            if i >= 0:
                x = int(a[i])
            else:
                x = 0

            if j >= 0:
                y = int(b[j])
            else:
                y = 0

            temp_sum = x + y + carry_bit

            return_list = str(temp_sum % 2) + return_list
            carry_bit = temp_sum // 2

            i -= 1
            j -= 1

        if carry_bit:
            return_list = "1" + return_list
            return return_list

        return return_list
# @lc code=end


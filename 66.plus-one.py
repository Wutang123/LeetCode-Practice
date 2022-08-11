#
# @lc app=leetcode id=66 lang=python3
#
# [66] Plus One
#

# @lc code=start
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:

        # Solution 1:
        # Time Complexity: O(n), where n is the length of digits
        # Space Complexity: O(n)

        # Start for loop at the end of the list
        for i in range(len(digits) - 1, -1, -1):

            if digits[i] != 9:
                digits[i] += 1
                return digits

            # If value is equal to 9 then set it to 0
            else:
                digits[i] = 0
                # If index is the first value then change to 0 and insert a 1 at the first index
                if i == 0:
                    digits.insert(0, 1)
                    return digits

# @lc code=end


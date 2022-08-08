#
# @lc app=leetcode id=412 lang=python3
#
# [412] Fizz Buzz
#

# @lc code=start
class Solution:
    def fizzBuzz(self, n: int) -> List[str]:

        # Solution 1:
        # Time Complexity: O(n)
        # Space Complexity: O(1)

        ret_array = []

        for i in range(1, n + 1):

            # If divisible by both 3 and 5
            if (i % 5 == 0 and i % 3 == 0):
                ret_array.append("FizzBuzz")

            # If divisible by 3
            elif (i % 3 == 0):
                ret_array.append("Fizz")

            # If divisible by 5
            elif (i % 5 == 0):
                ret_array.append("Buzz")

            # If not divisible by either 3 or 5
            else:
                ret_array.append(str(i))

        return ret_array

# @lc code=end


#
# @lc app=leetcode id=1480 lang=python3
#
# [1480] Running Sum of 1d Array
#

# @lc code=start
class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:

        # Solution 1:
        # Time Complexity: O(n)
        # Space Complexity: O(1)

        temp_value = 0
        return_array = []

        for count, value in enumerate(nums):
            return_array.append(temp_value + value)
            temp_value = return_array[count]

        return return_array

# @lc code=end


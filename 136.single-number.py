#
# @lc app=leetcode id=136 lang=python3
#
# [136] Single Number
#

# @lc code=start
class Solution:
    def singleNumber(self, nums: List[int]) -> int:

        # Solution 1:
        # Time Complexity: O(n), where n is the length of nums
        # Space Complexity: O(n), where n is the length of nums

        dict_num = {}

        for i in range(0, len(nums)):
            dict_num[nums[i]] = dict_num.get(nums[i], 0) + 1

        for key, value in dict_num.items():
            if value == 1:
                return key

# @lc code=end


#
# @lc app=leetcode id=1 lang=python3
#
# [1] Two Sum
#

# @lc code=start
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        # Solution 1: (Brute Force)
        # Time Complexity O(n^2)
        # Space Complexity O(1)

        # for i, i_val in enumerate(nums):
        #     for j, j_val in enumerate(nums[i + 1:]):
        #         if (i_val + j_val == target):
        #             return [i, i + j + 1]

        # Solution 2: (Hash Map)
        # Time Complexity: O(n)
        # Space Complexity O(n)

        prev_map = {} # val : index

        for i, val in enumerate(nums):
            difference = target - val
            if difference in prev_map:
                return [prev_map[difference], i]
            prev_map[val] = i


# @lc code=end


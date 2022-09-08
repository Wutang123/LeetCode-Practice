#
# @lc app=leetcode id=217 lang=python3
#
# [217] Contains Duplicate
#

# @lc code=start
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:

        # Solution 1: Sorting
        # Time Complexity: O(n), where n is the length of list
        # Space Complexity: O(1)

        # nums.sort()

        # temp = nums[0]
        # for i in range(1, len(nums)):
        #     if nums[i] == temp:
        #         return True

        #     temp = nums[i]

        # return False

        # Solution 2: Set()
        # Time Complexity: O(1)
        # Space Complexity: O(n)

        nums_set = set(nums)

        if len(nums) == len(nums_set):
            return False
        return True

# @lc code=end


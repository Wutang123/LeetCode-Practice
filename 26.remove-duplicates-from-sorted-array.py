#
# @lc app=leetcode id=26 lang=python3
#
# [26] Remove Duplicates from Sorted Array
#

# @lc code=start
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:

        # Solution 1: (Replacing w/ out of bounds value)
        # Time Complexity: O(N), where N is the nums length
        # Space Complexity: O(1)

        k = 0
        for i in range(0, len(nums) - 1):

            if nums[i] == nums[i + 1]:

                nums[i] = 999
            else:
                k += 1

        k += 1
        nums.sort()

        return k


        # Solution 2: (Using pop ())
        # Time Complexity: O(N), where N is the nums length
        # Space Complexity: O(1)
#         i = 1
#         while i < len(nums):
#             if nums[i] == nums[i - 1]:
#                 nums.pop(i)
#             else:
#                 i += 1

#         return len(nums)

# @lc code=end


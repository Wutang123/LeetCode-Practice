#
# @lc app=leetcode id=35 lang=python3
#
# [35] Search Insert Position
#

# @lc code=start
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:

        # Solution 1: (Binary Search)
        # Time Complexity: O(logn)
        # Space Complexity: O(1)

        # len_list = len(nums) - 1 # Length of list of list is used for indexing
        # i_0 = 0
        # i_n = len_list

        # while i_0 < i_n:

        #     mid_val = (i_0 + i_n)//2

        #     if nums[mid_val] == target:
        #         return mid_val

        #     # Move lower bound above midpoint
        #     if nums[mid_val] < target:
        #         i_0 = mid_val + 1

        #     # Move upper bound above midpoint
        #     if nums[mid_val] > target:
        #         i_n = mid_val - 1

        # mid_val = (i_0 + i_n)//2

        # # If out of bound (negative), rebound to zero
        # if mid_val < 0:
        #     mid_val = 0

        # # Edge Case
        # # If on lower bound and target is less than lowest bound, then return lowest bound
        # if mid_val == 0 and nums[mid_val] > target:
        #     return 0

        # # If on lower bound and target is greater than lowest bound, then return lowest bound + 1
        # if mid_val == 0 and nums[mid_val] < target:
        #     return 1

        # # If on larger bound and target is less than lowest bound, then return largest bound
        # if mid_val == len_list and nums[mid_val] > target:
        #     return mid_val

        # # If on larger bound and target is greater than lowest bound, then return largest bound + 1
        # if mid_val == 0 and nums[mid_val] < target:
        #     return mid_val + 1

        # # Recheck
        # if nums[mid_val] < target:
        #     return mid_val + 1

        # if nums[mid_val] > target:
        #     return mid_val

        # if nums[mid_val] == target:
        #         return mid_val

        # Solution 2: (Binary Search) - Simplified
        # Time Complexity: O(logn)
        # Space Complexity: O(1)

        i_0 = 0
        i_n = len(nums) - 1

        while i_0 <= i_n:

            mid_val = (i_0 + i_n)//2

            if nums[mid_val] == target:
                return mid_val

            # Move lower bound above midpoint
            if nums[mid_val] < target:
                i_0 = mid_val + 1

            # Move upper bound above midpoint
            if nums[mid_val] > target:
                i_n = mid_val - 1

        return i_0


# @lc code=end


#
# @lc app=leetcode id=219 lang=python3
#
# [219] Contains Duplicate II
#

# @lc code=start
class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:

        # Solution 1: For loop - too slow, won't complete
        # Time Complexity: O(n^2), where n is the length of nums
        # Space Complexity: O(1)

        # # Edge Case:
        # if len(nums) <= 1:
        #     return False

        # for i in range (0, len(nums)):
        #     for j in range (i + 1, len(nums)):
        #         if nums[i] == nums[j]:
        #             if abs(i - j) <= k:
        #                 return True

        # return False

        # Solution 2:
        # Time Complexity: O(n), where n is the length of list
        # Space Complexity: O(n), where n is the length of list

        # Edge Case: (No Duplicates)
        if len(nums) <= 1:
            return False

        if len(nums) == len(set(nums)):
            return False

        index_dict = {}

        for i in range(0, len(nums)):
            if nums[i] not in index_dict:
                index_dict[nums[i]] = i
            else:
                if abs(i - index_dict[nums[i]]) <= k:
                    return True
                else:
                    index_dict[nums[i]] = i

        return False

# @lc code=end


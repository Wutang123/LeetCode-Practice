#
# @lc app=leetcode id=27 lang=python3
#
# [27] Remove Element
#

# @lc code=start
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:

        # Solution 1: (Pop Method)
        # Time Complexity: O(n)
        # Space Complexity: O(1)

        i        = 0 # List index
        count    = 0
        orig_len = len(nums)

        while count < orig_len:
            if nums[i] == val:
                nums.pop(i)
            else:
                # Update index if values are not the same
                i += 1

            # Count each iteration
            count += 1

        return len(nums)

# @lc code=end


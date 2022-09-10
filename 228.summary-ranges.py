#
# @lc app=leetcode id=228 lang=python3
#
# [228] Summary Ranges
#

# @lc code=start
class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:

        # Solution 1:
        # Time Complexity: O(n), where n is the length of nums
        # Space Complexity: O(n), where n is the length of nums

        # Edge Case:
        if not nums:
            return nums

        ret = []
        temp_start = nums[0]
        temp_end = nums[0]

        for i in range(1, len(nums)):

            # Check if the next value comes after the previous
            if temp_end + 1 == nums[i]:
                temp_end = nums[i]
            else:
                if temp_start == temp_end:
                    ret.append(str(temp_start))
                else:
                    ret.append(str(temp_start) + "->" + str(temp_end))

                # Reset temp
                temp_start = nums[i]
                temp_end = nums[i]

        # Append the last grouping
        if temp_start == temp_end:
            ret.append(str(temp_start))
        else:
            ret.append(str(temp_start) + "->" + str(temp_end))

        return ret


# @lc code=end


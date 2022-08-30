#
# @lc app=leetcode id=169 lang=python3
#
# [169] Majority Element
#

# @lc code=start
class Solution:
    def majorityElement(self, nums: List[int]) -> int:

        # Solution 1:
        # Time Complexity: O(nlogn), where n is the length of list
        # Space Complexity: O(1)

        majority = -(-len(nums) // 2) # Do ceiling division
        nums.sort()
        temp  = nums[0]
        count = 0

        for i in nums:
            if i != temp:
                temp = i
                count = 1

            else:
                count += 1

            if count >= majority:
                return temp


# @lc code=end


#
# @lc app=leetcode id=108 lang=python3
#
# [108] Convert Sorted Array to Binary Search Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:

        # Solution 1:
        # Time Complexity: O(n), where n is the number of nodes
        # Space Complexity: O(n), where n is the number of nodes

        if not nums:
            return None

        mid = len(nums)//2
        node = TreeNode(nums[mid])

        node.left  = self.sortedArrayToBST(nums[0:mid])
        node.right = self.sortedArrayToBST(nums[mid+1:len(nums)])

        return node

# @lc code=end


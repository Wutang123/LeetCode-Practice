#
# @lc app=leetcode id=112 lang=python3
#
# [112] Path Sum
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:

        # Solution 1:
        # Time Complexity: O(n), where n is the number of nodes
        # Space Complexity: O(1)

        if not root:
            return False

        if root.left == None and root.right == None :
            if targetSum - root.val == 0:
                return True

            return False

        return self.hasPathSum(root.left, targetSum - root.val) or self.hasPathSum(root.right, targetSum - root.val)



# @lc code=end


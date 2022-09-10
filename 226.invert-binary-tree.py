#
# @lc app=leetcode id=226 lang=python3
#
# [226] Invert Binary Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:

        # Solution 1:
        # Time Complexity: O(n), where n is the number of nodes
        # Space Complexity: O(1)

        # Edge Case
        if not root:
            return root

        # Create queue
        queue = []
        queue.append(root)

        while queue:
            current_node = queue.pop(0)

            # Hold temp values of each node
            temp_right = current_node.right
            temp_left = current_node.left

            # Invert Left and Right Nodes
            current_node.left = temp_right
            current_node.right = temp_left

            # Continue Adding to Queue
            if current_node.left:
                queue.append(current_node.left)

            if current_node.right:
                queue.append(current_node.right)

        return root

# @lc code=end


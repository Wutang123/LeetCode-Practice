#
# @lc app=leetcode id=104 lang=python3
#
# [104] Maximum Depth of Binary Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:

        # Solution 1: (Recursive)
        # Time Complexity: O(n), where n is the number of nodes
        # Space Complexity: O(1)

        # if not root:
        #     return 0

        # return max(self.maxDepth(root.left), self.maxDepth(root.right)) + 1

        # Solution 2: (Iterative)
        # Time Complexity: O(n), where n is the number of nodes
        # Space Complexity: O(1)

        if not root:
            return 0

        worklist = deque([root])
        num_node_level = 1
        levels = 0

        while worklist:
            node = worklist.popleft()

            if node.left:
                worklist.append(node.left)

            if node.right:
                worklist.append(node.right)

            num_node_level -= 1
            if num_node_level == 0:
                levels += 1
                num_node_level = len(worklist)

        return levels

# @lc code=end


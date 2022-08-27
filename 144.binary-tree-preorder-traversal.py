#
# @lc app=leetcode id=144 lang=python3
#
# [144] Binary Tree Preorder Traversal
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:

        # Solution 1: Recursive
        # Time Complexity: O(n), where n is the number of nodes
        # Space Complexity: O(n), where n is the number of nodes

        # def preorder(node, ret):
        #     if not node:
        #         return

        #     ret.append(node.val)
        #     preorder(node.left, ret)
        #     preorder(node.right, ret)

        #     return ret

        # ret = []
        # return preorder(root, ret)

        # Solution 2: Iterative
        # Time Complexity: O(n), where n is the number of nodes
        # Space Complexity: O(n), where n is the number of nodes

        ret = []
        queue = deque()
        queue.append(root)

        while queue:
            temp = queue.pop()
            if temp:
                ret.append(temp.val)
                queue.append(temp.right)
                queue.append(temp.left)
        return ret


# @lc code=end


#
# @lc app=leetcode id=145 lang=python3
#
# [145] Binary Tree Postorder Traversal
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:

        # Solution 1: Recursive
        # Time Complexity: O(n), where n is the number of nodes
        # Space Complexity: O(n), where n is the number of nodes
        # def post(node, ret):
        #     if not node:
        #         return

        #     post(node.left, ret)
        #     post(node.right, ret)
        #     ret.append(node.val)

        #     return ret

        # ret = []
        # return post(root, ret)

        # Solution 2: Iterative
        # Time Complexity: O(n), where n is the number of nodes
        # Space Complexity: O(n), where n is the number of nodes

        ret = []
        queue = []
        queue.append(root)

        while queue:
            temp = queue.pop()
            if temp:
                queue.append(temp.left)
                queue.append(temp.right)
                ret.insert(0, temp.val)
        return ret

# @lc code=end


#
# @lc app=leetcode id=100 lang=python3
#
# [100] Same Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:

        # Solution 1: (Preorder)
        # Time Complexity: O(n), where n is the number of nodes in both trees
        # Space Complexity: O(n), where n is the number of nodes in both trees

        # def preorder(node, ret):
        #     if node:
        #         ret.append(node.val)
        #         preorder(node.left, ret)
        #         preorder(node.right, ret)
        #     else:
        #         ret.append('null')

        #     return ret

        # ret = []
        # preorder_p = preorder(p, ret)
        # ret = []
        # preorder_q = preorder(q, ret)

        # if preorder_p == preorder_q:
        #     return True
        # return False

        # Solution 2:
        # Time Complexity: O(n), where n is the number of nodes in both trees
        # Space Complexity: O(1)
        if not p and not q:
            return True
        elif not p or not q:
            return False
        else:
            return p.val == q.val and self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)

# @lc code=end


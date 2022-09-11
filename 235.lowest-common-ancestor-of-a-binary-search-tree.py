#
# @lc app=leetcode id=235 lang=python3
#
# [235] Lowest Common Ancestor of a Binary Search Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':

        # Solution 1:
        # Time Complexity: O(n), where n is the number of nodes
        # Space Complexity: O(1)

        # def find_lca(node, p, q):
        #     if node == p or node == q or not node:
        #         return node

        #     left = find_lca(node.left, p, q)
        #     right = find_lca(node.right, p, q)

        #     if left and right:
        #         return node
        #     elif left:
        #         return left
        #     elif right:
        #         return right

        #     return None

        # return find_lca(root, p, q)

        # Solution 2:
        # Time Complexity: O(logn), where n is the number of nodes (height of the tree)
        # Space Complexity: O(1)

        if max(p.val, q.val) < root.val:
            return self.lowestCommonAncestor(root.left, p, q)
        elif min(p.val, q.val) > root.val:
            return self.lowestCommonAncestor(root.right, p, q)
        else:
            return root

# @lc code=end


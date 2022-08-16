#
# @lc app=leetcode id=101 lang=python3
#
# [101] Symmetric Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:

        # Solution 1: (Modified preorder)
        # Time Complexity: O(n), where n is the number of nodes
        # Space Complexity: O(n), where n is the number of nodes
        # def preorder_left(node, ret):
        #     if node:
        #         ret.append(node.val)
        #         preorder_left(node.left, ret)
        #         preorder_left(node.right, ret)
        #     else:
        #         ret.append('null')

        #     return ret

        # def preorder_right(node, ret):
        #     if node:
        #         ret.append(node.val)
        #         preorder_right(node.right, ret)
        #         preorder_right(node.left, ret)
        #     else:
        #         ret.append('null')

        #     return ret

        # ret = []
        # root_left = preorder_left(root.left, ret)
        # ret = []
        # root_right = preorder_right(root.right, ret)

        # if root_left == root_right:
        #     return True
        # return False

        # Solution 2: (Recursive)
        # Time Complexity: O(n), where n is the number of nodes
        # Space Complexity: O(1)

        def Symmetric_check(root1, root2):

            if root1 == None and root2 == None:
                return True

            if (root1 != None and root2 != None) and (root1.val == root2.val):
                return Symmetric_check(root1.left, root2.right) and Symmetric_check(root1.right, root2.left)

            return False

        return Symmetric_check(root, root)

# @lc code=end


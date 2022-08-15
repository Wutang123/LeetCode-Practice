#
# @lc app=leetcode id=94 lang=python3
#
# [94] Binary Tree Inorder Traversal
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:

        # Solution 1: (Recursive)
        # Time Complexity: O(n)
        # Space Complexity: O(n)

        # ret_list = []
        # def inorder(node):

        #     if not node:
        #         return

        #     inorder(node.left)
        #     ret_list.append(node.val)
        #     inorder(node.right)

        # inorder(root)
        # return ret_list

        # Solution 2: (Stack)
        # Time Complexity: O(n)
        # Space Complexity: O(n)

        stack = [ (False, root) ]
        ret_list = []

        while stack:
            flag, val = stack.pop()

            if val:
                if not flag:
                    stack.append( (False, val.right) )
                    stack.append( (True, val       ) )
                    stack.append( (False, val.left ) )
                else:
                    ret_list.append( val.val )

        return ret_list

# @lc code=end


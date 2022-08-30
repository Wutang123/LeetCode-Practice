#
# @lc app=leetcode id=160 lang=python3
#
# [160] Intersection of Two Linked Lists
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:

        # Solution 1:
        # Time Complexity: O(m + n), where m is the number of nodes in list A and n is the number of nodes in list B
        # Space Complexity: O(1)

        a = headA
        b = headB

        while a != b:

            if not a:
                a = headB
            else:
                a = a.next

            if not b:
                b = headA
            else:
                b = b.next

        return a
# @lc code=end


#
# @lc app=leetcode id=206 lang=python3
#
# [206] Reverse Linked List
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        # Solution 1: Recursive
        # Time Complexity:
        # Space Complexity:

        def reverse(current, prev):

            if not current:
                return prev

             # Use 3 pointers to traverse the list and swap directions
            next_node = current.next
            current.next = prev
            return reverse(next_node, current)

        prev = None
        current = head
        return reverse(current, prev)


        # Solution 2: Iterative
        # Time Complexity: O(n)
        # Space Complexity: O(1)

        # # Edge Case
        # if head is None or head.next is None:
        #     return head

        # prev = None
        # current = head

        # # Use 3 pointers to traverse the list and swap directions
        # while current:
        #     next_node = current.next
        #     current.next = prev
        #     prev = current
        #     current = next_node

        # return prev



# @lc code=end


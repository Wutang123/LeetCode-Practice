#
# @lc app=leetcode id=203 lang=python3
#
# [203] Remove Linked List Elements
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        # Solution 1:
        # Time Complexity: O(n), where n is the number of nodes
        # Space Complexity: O(1)

        # If head exists
        if head:

            # Create a current and previous pointer
            temp_curr = head.next
            temp_prev = head
            while temp_curr != None:

                # If current node is the val then the previous node next is the current node next
                if temp_curr.val == val:
                    temp_prev.next = temp_curr.next
                else: # Else move previous pointer forward
                    temp_prev = temp_curr

                # Move current pointer forward
                temp_curr = temp_curr.next

            # Check if head node is the val
            if head.val == val:
                head = head.next

        return head



# @lc code=end


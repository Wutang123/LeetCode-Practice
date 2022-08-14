#
# @lc app=leetcode id=83 lang=python3
#
# [83] Remove Duplicates from Sorted List
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:

        # Solution 1:
        # Time Complexity: # O(n), where n is the number of nodes
        # Space Complexity: # O(1)

        # Edge Case:
        # Return head if list is empty or only contains 1 node
        if not head or not head.next:
            return head

        # Initalize two pointers to help tranverse
        temp_head_1 = head
        temp_head_2 = head
        val = head.val

        while temp_head_2.next:
            # If the next node is different than the compare value
                # Update the value and skip over the same value nodes
            if temp_head_2.val != val:
                val = temp_head_2.val
                temp_head_1.next = temp_head_2
                temp_head_1 = temp_head_1.next

            temp_head_2 = temp_head_2.next

        # Re-check last nodes in list for duplicates
        if temp_head_2.val != val:
            temp_head_1.next = temp_head_2
        else:
            temp_head_1.next = temp_head_2.next

        return head

# @lc code=end


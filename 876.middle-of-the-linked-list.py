#
# @lc app=leetcode id=876 lang=python3
#
# [876] Middle of the Linked List
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:

        # Solution 1:
        # Time Complexity: O(n)
        # Space Complexity: O(n)

        length = 1
        temp_list = head

        while temp_list.next != None:
            temp_list = temp_list.next
            length += 1

        middle = length//2

        temp_list = head
        i = 0

        while(i < middle):
            temp_list = temp_list.next
            i += 1

        return temp_list

# @lc code=end


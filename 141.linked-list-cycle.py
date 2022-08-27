#
# @lc app=leetcode id=141 lang=python3
#
# [141] Linked List Cycle
#

# @lc code=start

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:

        # Solution 1: (Dictionary)
        # Time Complexity: O(n), where n is the length of linked list
        # Space Complexity: O(n), where n is the length of linked list

        dict_node = {}
        temp = head

        while temp:
            if temp in dict_node:
                return True
            else:
                    dict_node[temp]= True
            temp = temp.next
        return False

        # Solution 2: (Slow-Fast)
        # Time Complexity: O(n), where n is the length of linked list
        # Space Complexity: O(1)

        # Edge Case
        # if not head:
        #     return False

        # slow = head
        # fast = head.next

        # while slow and fast and fast != slow and fast.next:
        #     slow = slow.next
        #     fast = fast.next.next

        # if slow == fast:
        #    return True

        # return False

# @lc code=end


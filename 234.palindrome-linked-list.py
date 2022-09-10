#
# @lc app=leetcode id=234 lang=python3
#
# [234] Palindrome Linked List
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:

        # Solution 1: TIME LIMIT EXCEEDED
        # Time Complexity: O(n^2)
        # Space Complexity: O(1)

        # Find last node
        # def last_node(node):
        #     if not node.next or node.next.val == None:
        #         temp = node.val
        #         node.val = None
        #         return temp
        #     return last_node(node.next)

        # while head.next:
        #     if head.val != last_node(head):
        #         return False
        #     else:
        #         head = head.next

        # return True

        # Solution 2:
        # Time Complexity: O(n)
        # Space Complexity: O(1)

        def reverse(current, previous):
            if not current:
                return previous

            current_next = current.next
            current.next = previous
            return reverse(current_next, current)

        def check_paliindrome(head, middle):
            if (not middle):
                return True
            elif (head.val == middle.val):
                return check_paliindrome(head.next, middle.next)
            else:
                return False

        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # Reverse the back half of the linked list
        middle = reverse(slow, None)
        return check_paliindrome(head, middle)


# @lc code=end


#
# @lc app=leetcode id=202 lang=python3
#
# [202] Happy Number
#

# @lc code=start
class Solution:
    def isHappy(self, n: int) -> bool:

        # Solution 1: Dictionary
        # Time Complexity: O()
        # Space Complexity: O()

        # seen = {}
        # total = 0

        # while n != 1:
        #     seen[n] = n

        #     while n:
        #         total += (n % 10) ** 2
        #         n = n // 10

        #     n = total
        #     if n in seen:
        #         return False
        #     total = 0

        # return True

        # Solution 2:
        # Time Complextiy: O(logn)
        # Space Complexity: O(1)

        def happy(num):
            total = 0
            while num:
                total += (num % 10) ** 2
                num = num // 10
            return total

        slow = n
        fast = happy(n)

        # Loop until either fast equals slow or fast equals 1
        while slow != fast and fast != 1:
            slow = happy(slow)
            fast = happy(happy(fast))

        if fast == 1:
            return True
        else:
            return False


# @lc code=end


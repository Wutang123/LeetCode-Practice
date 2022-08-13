#
# @lc app=leetcode id=69 lang=python3
#
# [69] Sqrt(x)
#

# @lc code=start
class Solution:
    def mySqrt(self, x: int) -> int:

        # Solution 1:
        # Time Complexity: O(n), where n is the sqrt(x)
        # Space Complexity: O(1)
        # root = 0
        # while (root + 1) * (root + 1) <= x:
        #     root += 1

        # return root

        # Solution 2: (Binary Search)
        # Time ComplexityL O(logn)
        # Space Complexity: O(1)

        # Initalize
        start = 0
        end = x
        mid = 0
        ans = 0

        while start <= end:

            # Find midpoint between two indexes
            mid = start + (end - start) // 2

            if (mid * mid <= x):
                ans = mid       # Keep track of the largest square root
                start = mid + 1
            else:
                end = mid - 1

        return ans



# @lc code=end


#
# @lc app=leetcode id=88 lang=python3
#
# [88] Merge Sorted Array
#

# @lc code=start
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """

        # Solution 1: (Simple)
        # Time Complexity: O(m+n), where m and n represent the number of elements in num1 and num2 respectively
        # Space Complexity: O(1)

        # if n:
        #     # Last n elements are set to zero, swap them with num2
        #     for i in range(0, n):
        #         nums1[-i - 1] = nums2[i]

        #     # Sort nums1
        #     nums1.sort()

        # Solution 2: (Start Backward)
        # Time Complexity: O(m+n), where m and n represent the number of elements in num1 and num2 respectively
        # Space Complexity: O(1)

        i = m - 1
        j = n - 1
        k = m + n - 1

        while j >= 0:
            if i >= 0 and nums1[i] > nums2[j]:
                nums1[k] = nums1[i]
                i -= 1
            else:
                nums1[k] = nums2[j]
                j -= 1

            k -= 1


# @lc code=end


#
# @lc app=leetcode id=190 lang=python3
#
# [190] Reverse Bits
#

# @lc code=start
class Solution:
    def reverseBits(self, n: int) -> int:

        # Solution 1: String Method
        # Time Complexity: O(logn), where n is 32
        # Space Complexity: O(n)

        # n_binary = format(n, "b") # Convert int to binary string
        # n_binary = n_binary.zfill(32) # Pad left with zeros (should be 32 bits)
        # n_binary = list(n_binary)

        # i = 0
        # j = len(n_binary) - 1

        # while i < j: # Two pointers (one at the begin and one at the end)

        #     # Bit Swap
        #     temp = n_binary[j]
        #     n_binary[j] = n_binary[i]
        #     n_binary[i] = temp

        #     i += 1
        #     j -= 1

        # ret_string = ''.join(n_binary) # Joint the string
        # ret = int(ret_string, 2) # Convert binary string to int

        # return ret

        # Solution 2: Bit Maniplulation:
        # Time Complexity: O(n), where n is 32
        # Space Complexity: O(1)

        ret = 0

        for i in range(0, 32):
            ret = ret << 1 # Shift left to have space for new bit
            bit = n % 2    # Get rightmost bit
            ret += bit     # Add bit to return value
            n = n >> 1     # Drop rightmost bit

        return ret
# @lc code=end


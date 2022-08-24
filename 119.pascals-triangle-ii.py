#
# @lc app=leetcode id=119 lang=python3
#
# [119] Pascal's Triangle II
#

# @lc code=start
class Solution:
    def getRow(self, rowIndex: int) -> List[int]:

        # Solutiom 1:
        # Time Complexity: O(n^2)
        # Space Complexity: O(n)

        if rowIndex == 0:
            return [1]

        if rowIndex == 1:
            return [1,1]

        ret_list = [1,1]

        for i in range(1, rowIndex):
            temp = []

            for j in range(0, i + 1):
                if j == 0:
                    temp.append(1)
                    continue

                temp.append(ret_list[j - 1] + ret_list[j])

                if j == i:
                    temp.append(1)

            ret_list = temp

        return ret_list

# @lc code=end


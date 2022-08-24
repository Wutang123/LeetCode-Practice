#
# @lc app=leetcode id=118 lang=python3
#
# [118] Pascal's Triangle
#

# @lc code=start
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:

        # Solution 1:
        # Time Complexity: O(n^2)
        # Space Complexity: O(n^2)

        if numRows == 1:
            return [[1]]

        if numRows == 2:
            return [[1],[1,1]]

        ret_list = [[1],[1,1]]

        for i in range(1, numRows - 1):
            temp = []

            for j in range (0, i + 1):
                if j == 0:
                    temp.append(1)
                    continue

                temp.append(ret_list[i][j - 1] + ret_list[i][j])

                if j == i:
                    temp.append(1)

            ret_list.append(temp)

        return ret_list

# @lc code=end


#
# @lc app=leetcode id=13 lang=python3
#
# [13] Roman to Integer
#

# Symbol       Value
# I             1
# V             5
# X             10
# L             50
# C             100
# D             500
# M             1000

# I can be placed before V (5) and X (10) to make 4 and 9. 
# X can be placed before L (50) and C (100) to make 40 and 90. 
# C can be placed before D (500) and M (1000) to make 400 and 900.

# @lc code=start
class Solution:
    def romanToInt(self, s: str) -> int:
        
        # Solution 1: Brute Force
        # Time Complexity: O(n)
        # Space Complexity: O(1)
        # return_num = 0
        # continue_flag = False
        # s = s + '0'
        
        # for char in range(len(s)):
        #     if continue_flag:
        #         continue_flag = False
        #         continue
            
        #     if (s[char] == 'I'):
        #         if (s[char + 1] == 'V'):
        #             return_num += 4
        #             continue_flag = True
        #         elif (s[char + 1] == 'X'):
        #             return_num += 9
        #             continue_flag = True
        #         else:
        #             return_num += 1
                    
        #     elif (s[char] == 'V'):
        #         return_num += 5
                
        #     elif (s[char] == 'X'):
        #         if (s[char + 1] == 'L'):
        #             return_num += 40
        #             continue_flag = True
        #         elif (s[char + 1] == 'C'):
        #             return_num += 90
        #             continue_flag = True
        #         else:
        #             return_num += 10
                    
        #     elif (s[char] == 'L'):
        #         return_num += 50
                
        #     elif (s[char] == 'C'):
        #         if (s[char + 1] == 'D'):
        #             return_num += 400
        #             continue_flag = True
        #         elif (s[char + 1] == 'M'):
        #             return_num += 900
        #             continue_flag = True
        #         else:
        #             return_num += 100
                    
        #     elif (s[char] == 'D'):
        #         return_num += 500
                
        #     elif (s[char] == 'M'):
        #         return_num += 1000
        
        # return return_num
        
        #-----------------------------------------------------------------
        
        # Solution 2: (Replacing)
        # Time Complexity: O(n)
        # Space Complexity: O(1)
        translations = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }
        
        return_num = 0
        
        s = s.replace("IV", "IIII").replace("IX", "VIIII")
        s = s.replace("XL", "XXXX").replace("XC", "LXXXX")
        s = s.replace("CD", "CCCC").replace("CM", "DCCCC")
        
        for char in s:
            return_num += translations[char]
            
        return return_num
        
# @lc code=end


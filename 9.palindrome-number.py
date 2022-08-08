#
# @lc app=leetcode id=9 lang=python3
#
# [9] Palindrome Number
#

# @lc code=start
class Solution:
    def isPalindrome(self, x: int) -> bool:
        
        # Solution 1: (string conversion)
        # Time Complexity: O(n)
        # Space Complexity: O(n)
        
        # # Convert number to string array
        # temp_x = str(x)
        
        # # Special Case:
        # # - If less then 0 
        # # - If the last digit is 0
        # if (x < 0 or (x % 10 == 0 and x != 0)):
        #     return False
        
        # else:
        #     for i in range(0, len(temp_x)//2):
                
        #         # Compare first index with last index, then continue inwards
        #         if(temp_x[i] != temp_x[-(i+1)]):
        #             return False
                
        #     return True
        
        #--------------------------------------------------------------
        
        # Solution 2: (reverting half)
        # Time Complexity: 
        # Space Complexity:
        
        # Special Case:
        # - If less then 0 
        # - If the last digit is 0
        if (x < 0 or (x % 10 == 0 and x != 0)):
            return False
        
        else:
            
            
            result = 0 
            while x > result:
                # Compare last half of num with the first half and determin if
                    # palindrome
                    
                # e.g 1221
                    # iter 1: num = 1221; result = 1
                    # iter 2: num = 122;  result = 12
                    # iter 3: num = 12;   result = 122
                result = (x % 10) + (result * 10)
                x = x // 10
                
            # If the num is even length than compare normally
            # If the num is odd length than divide result by 10
            if (x == result or x == result // 10):
                return True
         
        
# @lc code=end


#
# @lc app=leetcode id=383 lang=python3
#
# [383] Ransom Note
#

# @lc code=start
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
    
        # 1st solution
        # Time Complexity: O(n*m)
        # Space Complexity: O(1)
        # for i in range(len(magazine)):
        
        #     for j in range(len(ransomNote)):
        
        #         if magazine[i] == ransomNote[j]:
        #             ransomNote = ransomNote.replace(magazine[i], "", 1) 
                    
        #             if (not len(ransomNote)):
        #                 return True
        #             break
        
        # return False
    
    
        # 2nd solution
        # Time Complexity: O(n)
        # Space Complexity: O(1)
        for i in ransomNote:
            if i in magazine:
                magazine = magazine.replace(i, "", 1)
            else:
                return False
        return True          
  
# @lc code=end



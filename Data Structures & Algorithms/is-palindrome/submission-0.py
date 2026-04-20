import re
class Solution:
    def isPalindrome(self, s: str) -> bool:
        s1 = ""
        for c in s:
            if c.isalnum():
                s1 += c
        
        s2 = s1[::-1]
        if s1.lower() == s2.lower():
            return True
        else:
            return False        
        
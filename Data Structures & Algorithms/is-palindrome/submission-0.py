class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        b = 0 
        l = len(s) - 1

        while b < l:

            if (not s[b].isalnum()):
                b += 1
                continue
            if (not s[l].isalnum()):
                l -= 1
                continue
            if (s[b].lower() == s[l].lower()):
                b +=1 
                l -= 1
            else: 
                return False

        return True            
                        


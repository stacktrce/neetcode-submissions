class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        hs, ht = [], []

        for i in s:
            hs.append(i)
        for i in t:
            ht.append(i)

        if (sorted(hs) == sorted(ht)):
            return True        
            
        return False
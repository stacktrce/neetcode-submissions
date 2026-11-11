class Solution:
    def partition(self, s: str) -> List[List[str]]:
        
        res = []

        def isPalindrome(string):
            p1 = 0
            p2 = len(string) - 1

            while p1 < p2:
                if not ( string[p1] == string[p2]):
                    return False
                else: 
                    p1 += 1
                    p2 -= 1
            
            return True 


        def dfs(start, curr):
            
            if (start == len(s)):
                res.append(curr.copy())
                return

            for i in range(start, len(s)):

                if (len(curr) == len(s)):
                    continue

                #wenn curr kein palindrom hier verwerfen?
                if not (isPalindrome(s[start: i+1])):
                     
                     continue
                curr.append(s[start:i+1])
                dfs(i + 1, curr)
                curr.pop()
        dfs(0 , [])
        return res
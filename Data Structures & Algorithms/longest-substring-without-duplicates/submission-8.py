class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        counter = 0
        seen = set()

        p1, p2 = 0, 0

        for p2 in range(len(s)):

            while s[p2] in seen:
                seen.remove(s[p1])
                p1 += 1
            seen.add(s[p2])
            if (p2 - p1 + 1 > counter):
                counter = p2 - p1 + 1
            
        return counter

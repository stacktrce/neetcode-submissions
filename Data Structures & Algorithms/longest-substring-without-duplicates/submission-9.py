class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        res = 1
        l , r = 0, 0
        seen = set()

        if not s:
            return 0

        if len(s) == 1:
            return 1

        while r < len(s):
            if s[r] not in seen:
                seen.add(s[r])
                res = max(res, r - l + 1)
                r += 1
            else:
                seen.remove(s[l])
                l += 1

        return res

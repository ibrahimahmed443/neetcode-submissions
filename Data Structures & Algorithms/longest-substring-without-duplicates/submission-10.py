class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        maxL = 0
        l = 0
        map = {}

        for r in range(len(s)):
            if s[r] in map:
                l = max(map[s[r]] + 1, l)
            
            map[s[r]] = r
            maxL = max(maxL, r - l + 1)
        
        return maxL
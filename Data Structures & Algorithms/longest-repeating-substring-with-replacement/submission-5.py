class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        maxL = 0

        for l in range(len(s)):
            count = {}
            mostFrequent = 0
            for r in range(l, len(s)):
                count[s[r]] = 1 + count.get(s[r], 0)
                mostFrequent = max(mostFrequent, count[s[r]])

                if (r - l + 1) - mostFrequent <= k:
                    maxL = max(maxL, r - l + 1)
                else:
                    break
            
        return maxL
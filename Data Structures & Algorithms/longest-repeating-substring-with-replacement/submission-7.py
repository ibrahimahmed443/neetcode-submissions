class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        maxL = 0
        count = {}

        l = 0
        for r in range(len(s)):
            count[s[r]] = 1 + count.get(s[r], 0)

            while (r - l + 1) - max(count.values()) > k:
                count[s[l]] -= 1
                l += 1

            maxL = max(maxL, r - l + 1)

        return maxL
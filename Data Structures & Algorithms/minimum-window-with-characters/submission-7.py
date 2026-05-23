class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "":
            return ""

        count_t, count_window = {}, {}
        for c in t:
            count_t[c] = count_t.get(c, 0) + 1

        best_window = ""
        min_l = float('inf')
        have = 0
        need = len(count_t)

        l = 0
        for r in range(len(s)):
            c = s[r]
            count_window[c] = count_window.get(c, 0) + 1

            if c in count_t and count_window[c] == count_t[c]:
                have += 1
            
            while have == need:
                # we found a potential window
                if (r - l + 1) < min_l:
                    min_l = r - l + 1
                    best_window = s[l:r+1]
                
                # move from left to try to find a better (smaller) window
                count_window[s[l]] -= 1

                if s[l] in count_t and count_window[s[l]] < count_t[s[l]]:
                    have -= 1
                l += 1

        return best_window if min_l != float('inf') else ''
        
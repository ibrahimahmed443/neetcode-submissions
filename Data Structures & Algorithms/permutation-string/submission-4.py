from itertools import permutations

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        countS1 = self.findCount(s1)

        l = 0
        counts = {}
        for r in range(len(s1) - 1, len(s2)):
            seq = s2[l:r+1]

            if l == 0:
                countSeq = self.findCount(seq)
            else:
                countSeq[s2[r]] = 1 + countSeq.get(s2[r], 0)
                if countSeq[s2[l-1]] > 1:
                    countSeq[s2[l-1]] -= 1
                else:
                    countSeq.pop(s2[l-1])

            if countSeq == countS1:
                return True
            
            l += 1

        return False

    def findCount(self, s):
        count = {}
        for c in s:
            count[c] = 1 + count.get(c, 0)

        return count

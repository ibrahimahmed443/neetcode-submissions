from itertools import permutations

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        countS1 = self.findCount(s1)

        l = 0
        for r in range(len(s1) - 1, len(s2)):
            seq = s2[l:r+1]
            countSeq = self.findCount(seq)

            if countSeq == countS1:
                return True
            
            l += 1

        return False

    def findCount(self, s):
        count = {}
        for c in s:
            count[c] = 1 + count.get(c, 0)

        return count

from itertools import permutations

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        countS1 = {}
        countSeq = {}
        for i in range(len(s1)):
            countS1[s1[i]] = 1 + countS1.get(s1[i], 0)
            countSeq[s2[i]] = 1 + countSeq.get(s2[i], 0)

        l = 0
        for r in range(len(s1) - 1, len(s2)):
            seq = s2[l:r+1]

            if l > 0:       # update count for updated sequence
                countSeq[s2[r]] = 1 + countSeq.get(s2[r], 0)
                countSeq[s2[l-1]] -= 1
                if countSeq[s2[l-1]] == 0:
                    countSeq.pop(s2[l-1])

            if countSeq == countS1:
                return True
            
            l += 1

        return False

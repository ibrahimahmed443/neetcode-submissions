class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        start = math.ceil(sum(piles) / h)
        end = max(piles)
        res = end

        # Run a binary search through possible values of k
        while (start <= end):
            k = start + ((end - start) // 2)
            hrs = 0
            for bananas in piles:
                hrs += math.ceil(bananas/k)

            if hrs <= h:
                res = k
                end = k - 1
            else:
                start = k + 1

        return res
    
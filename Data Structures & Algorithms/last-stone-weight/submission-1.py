class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        while len(stones) > 1:
            x, y = self.findTwoHeaviestIndex(stones[:])
            if x == y:
                stones.pop(stones.index(x))
                stones.pop(stones.index(y))
            else:
                stones[stones.index(x)] = x - y
                stones.pop(stones.index(y))

        return stones[0] if len(stones) else 0

    def findTwoHeaviestIndex(self, stones):
        max1_index = 0
        for i, num in enumerate(stones):
            if num > stones[max1_index]:
                max1_index = i
        
        max1 = stones[max1_index]
        stones.pop(max1_index)
        
        max2 = stones[0]
        for i, num in enumerate(stones):
            if num > max2:
                max2 = num

        return max1, max2

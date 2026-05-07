class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        result = []

        for num in nums:
            count[num] = count.get(num, 0) + 1

        lst = [[count, num] for num, count in count.items()]
        lst.sort(key=lambda x: x[0])
        
        while len(result) < k:
            result.append(lst.pop()[1])

        return result
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        map = {}

        for num in nums:
            map[num] = 1 + map.get(num, 0)
        
        buckets = [[] for _ in range(max(map.values()))]

        for num, count in map.items():
            buckets[count-1].append(num)

        return self.getKRows(buckets, k)

    def getKRows(self, buckets, k):
        result = []
        for bucket in reversed(buckets):
            for num in bucket:
                result.append(num)
                if len(result) == k:
                    return result
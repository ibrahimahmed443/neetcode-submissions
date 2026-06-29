from collections import defaultdict

class TimeMap:

    def __init__(self):
        self.d = defaultdict(list)   # d = key: [<val, timestamp>,...]

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.d[key].append([value, timestamp])

    def get(self, key: str, timestamp: int) -> str:
        res = ""
        lst = self.d.get(key, [])

        left = 0
        right = len(lst) - 1

        while left <= right:
            mid = (left + right) // 2
            if lst[mid][1] == timestamp:
                res = lst[mid][0]
                break
            
            if lst[mid][1] < timestamp:
                res = lst[mid][0]
                left = mid + 1
            else:
                right = mid - 1
        
        return res



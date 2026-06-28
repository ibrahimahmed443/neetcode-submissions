class TimeMap:

    def __init__(self):
        self.d = {}
        self.timestamps = []

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.d[(key, timestamp)] = value

    def get(self, key: str, timestamp: int) -> str:
        if (key, timestamp) in self.d:
            # print(self.d.get((key, timestamp)))
            return self.d.get((key, timestamp))
        else:
            while timestamp >= 0:
                timestamp -= 1
                if (key, timestamp) in self.d:
                    return self.d.get((key, timestamp))
            return ""


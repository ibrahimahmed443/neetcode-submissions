class TimeMap:

    def __init__(self):
        self.d = {}
        self.timestamps = []

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.timestamps.append(timestamp)
        self.d[(key, timestamp)] = value

    def get(self, key: str, timestamp: int) -> str:
        if (key, timestamp) in self.d:
            return self.d.get((key, timestamp))
        else:
            for ts in self.timestamps[::-1]:
                if ts < timestamp and (key, ts) in self.d:
                    return self.d.get((key, ts))
            return ""


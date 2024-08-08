Link to the problem: https://leetcode.com/problems/time-based-key-value-store/
class TimeMap:

    def __init__(self):
        # key=string, value=list of [value,timestamp]
        self.store = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.store:
            self.store[key] = []
        self.store[key].append([value, timestamp])

    def get(self, key: str, timestamp: int) -> str:
        result = ''
        values = self.store.get(key,[])

        # Binary search
        l = 0
        r = len(values) - 1
        while l <= r:
            m = l + (r-l)//2
            if values[m][1] <= timestamp:
                result = values[m][0]
                l = m + 1
            else:
                r =m - 1
        return result

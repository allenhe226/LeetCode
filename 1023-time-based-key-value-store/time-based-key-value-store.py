class TimeMap:
    def __init__(self):
        self.values = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        l, r = 0, len(self.values[key])-1
        while l <= r:
            m = l+(r-l)//2
            if self.values[key][m][0] == timestamp:
                self.values[key].insert(m, (timestamp,value))
                return
            elif self.values[key][m][0] < timestamp:
                l = m+1
            else:
                r = m
        self.values[key].insert(l, (timestamp,value))
        

    def get(self, key: str, timestamp: int) -> str:
        l, r = 0, len(self.values[key])-1
        ans = -1
        while l <= r:
            m = l+(r-l)//2
            if self.values[key][m][0] <= timestamp:
                ans = m
                l = m+1
            else:
                r = m-1
        return self.values[key][ans][1] if ans != -1 else ""


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)
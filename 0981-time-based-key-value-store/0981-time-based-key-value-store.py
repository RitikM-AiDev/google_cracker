class TimeMap:

    def __init__(self):
        self.Key={}

    def set(self, key: str, value: str, timestamp: int) -> None:
            if key not in self.Key:
                self.Key[key] = []
            self.Key[key].append((timestamp,value))
            return

    def get(self, key: str, timestamp: int) -> str:
            if key not in self.Key:
                return ""
            i=0
            j=len(self.Key[key])-1
            ans=""
            while i<=j:
                mid = (i+j)//2
                if self.Key[key][mid][0]==timestamp:
                    return self.Key[key][mid][-1]
                elif self.Key[key][mid][0] < timestamp:
                    ans = self.Key[key][mid][-1]
                    i = mid + 1
                else:
                    j = mid-1
            return ans
# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)
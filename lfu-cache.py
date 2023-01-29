from collections import OrderedDict

# This solution is taken from this solution thread
# https://leetcode.com/problems/lfu-cache/solutions/3112035/python-simple-two-hash-maps-explained/
# in which I learned about Python's OrderedDict data structure

class LFUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.used = 0
        # keyToCount is indexed by keys, returns [val, count]
        self.keyToCount = {}
        # countToKeys is indexed by counts, returns OrderedDict of keys ordered by recency
        self.countToKeys = {}
        self.minCount = 0      

    def get(self, key: int) -> int:
        out = -1
        if key in self.keyToCount:
            out = self.keyToCount[key][0]
            pastCount = self.keyToCount[key][1]
            self.keyToCount[key][1] += 1

            del self.countToKeys[pastCount][key]
            self._updateCountToKeys(key, out, pastCount+1)

            if self.minCount == pastCount and len(self.countToKeys[pastCount]) == 0:
                self.minCount = pastCount + 1
        return out

    def put(self, key: int, value: int) -> None:
        if self.capacity <= 0:
            return
        
        if key in self.keyToCount:
            self.keyToCount[key][0] = value
            pastCount = self.keyToCount[key][1]
            self.keyToCount[key][1] += 1
            del self.countToKeys[pastCount][key]
            self._updateCountToKeys(key, value, pastCount+1)

            if self.minCount == pastCount and len(self.countToKeys[pastCount]) == 0:
                self.minCount = pastCount+1
        else:
            if self.used < self.capacity:
                self.keyToCount[key] = [value, 1]
                self._updateCountToKeys(key, value, 1)
                self.used += 1
                self.minCount = 1
            else:
                rmKey, rmVal = self.countToKeys[self.minCount].popitem(0)
                del self.keyToCount[rmKey]

                self.keyToCount[key] = [value, 1]
                self._updateCountToKeys(key, value, 1)
                self.minCount = 1

    def _updateCountToKeys(self, key, val, newCount):
        if newCount not in self.countToKeys:
            self.countToKeys[newCount] = OrderedDict()
        self.countToKeys[newCount][key] = val
        self.countToKeys[newCount].move_to_end(key)

# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
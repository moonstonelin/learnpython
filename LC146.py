class LRUCache(object):
    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.map = {}
        self.list = []
        self.maxSize = capacity
        self.curSize = 0

    def get(self, key):
        """
        :rtype: int
        """
        if key in self.map.keys():
            item = self.map[key]
            self.list.remove(item)
            self.list.insert(0, item)
            return item[1]
        else:
            return -1

    def set(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: nothing
        """
        if key in self.map.keys():
            item = self.map[key]
            self.list.remove(item)
            item = [key, value]
            self.list.insert(0, item)
            self.map[key] = item
        else:
            if self.curSize == self.maxSize:
                last = self.list.pop()
                del self.map[last[0]]
                self.curSize -= 1
            item = [key, value]
            self.list.insert(0, item)
            self.map[key] = item
            self.curSize += 1

cache = LRUCache(1)
cache.set(2, 1)
print cache.get(2)
cache.set(3, 2)
print cache.get(2)
print cache.get(3)
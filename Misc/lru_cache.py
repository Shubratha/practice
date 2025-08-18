from collections import OrderedDict


class LRUCache:
    def __init__(self, size=5):
        self.size = size
        self.cache = OrderedDict()

    def get(self, key):
        val = self.cache.get(key)
        if val:
            self.cache.move_to_end(key)
            return val
        else:
            return -1

    def put(self, key, val):
        if key in self.cache:
            print("Key already present")
            return

        self.cache[key] = val
        self.cache.move_to_end(key)
        if len(self.cache) > self.size:
            self.cache.popitem(last=False)

        return val


cache_obj = LRUCache()
val = cache_obj.get("a")
print(val)
cache_obj.put("b", "2")
print(cache_obj.cache)
print(cache_obj.get("b"))
cache_obj.put("a", "1")
cache_obj.put("c", "3")
cache_obj.put("d", "4")
cache_obj.put("e", "5")
cache_obj.put("f", "6")
print(cache_obj.cache)
print(cache_obj.get("b"))
print(cache_obj.get("d"))
print(cache_obj.cache)
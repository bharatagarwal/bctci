"""
# Hash Map Class

Implement a HashMap class with the API described here:

Map API:
- add(k, v): if k is not in the map, add key k to the map with
- value v. If k is already in the map, update its value to v.
- remove(k): if k is in the map, remove it from the map.
- contains(k): return whether the key k is in the map.
- get(k): return the value for key k. If k is not in the map, return a null value.
- size(): return the number of keys in the map.
"""


class HashMap:
    """
    >>> h = HashMap()
    >>> h.add(2, 5)
    >>> h.contains(2)
    True
    >>> h.contains(3)
    False
    >>> h.get(2)
    5
    >>> h.size()
    1
    """

    constant = 0.6180339

    def __init__(self):
        self.capacity = 10
        self._size = 0
        self.buckets = [None for _ in range(self.capacity)]

    def add(self, k, v):
        hash = self.hash(k, self.capacity)

        if not self.buckets[hash]:
            self._size += 1

        if self._load_factor() > 1:
            self.resize(self.capacity * 2)

        self.buckets[hash] = v

    def contains(self, k):
        return self.buckets[self.hash(k, self.capacity)] is not None

    def remove(self, k):
        hash = self.hash(k, self.capacity)

        if not self.buckets[hash]:
            return

        if self._load_factor() < 0.25:
            self.resize(self.capacity // 2)

        self.buckets[hash] = None
        self._size -= 1

    def get(self, k):
        return self.buckets[self.hash(k, self.capacity)]

    def size(self):
        return self._size

    def _load_factor(self):
        return self._size / self.capacity

    def _resize(self, new_capacity):
        new_buckets = [None for _ in range(new_capacity)]

        for i, bucket in enumerate(self.buckets):
            if bucket:
                new_buckets[self.hash(i, new_capacity)] = bucket

        self.buckets = new_buckets
        self.capacity = new_capacity

    def hash(self, k, capacity):
        k *= self.constant
        k -= int(k)
        k *= capacity

        return int(k)

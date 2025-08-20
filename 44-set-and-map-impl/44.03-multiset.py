"""
A multiset is a set that allows multiple copies of the same element. Implement a Multiset class with the following methods:

- add(x): adds a 'copy' of x to the multiset.
- remove(x): removes a 'copy' of x from the multiset.
- contains(x): return whether x is in the multiset (at least one copy).
- size(): return the number of elements in the multiset (including copies).
"""


class Multiset:
    constant = 0.6180339887

    def __init__(self):
        self.capacity = 10
        self.buckets = [[] for _ in range(self.capacity)]
        self._size = 0

    def add(self, x):
        h = self.hash(x, self.capacity)

        self.buckets[h].append(x)
        self._size += 1

        if self.load_factor() > 1:
            self.resize(self.capacity * 2)

    def contains(self, x):
        h = self.hash(x, self.capacity)
        return x in self.buckets[h]

    def remove(self, x):
        h = self.hash(x, self.capacity)

        if x in self.buckets[h]:
            self.buckets[h].remove(x)
            self._size -= 1

            if self.load_factor() < 0.25 and self.capacity > 10:
                self.resize(self.capacity // 2)

            return

    def size(self):
        return self._size

    def load_factor(self):
        return self._size / self.capacity

    def resize(self, new_capacity):
        new_buckets = [[] for _ in range(new_capacity)]

        for bucket in self.buckets:
            for elem in bucket:
                h = self.hash(elem, new_capacity)
                new_buckets[h].append(elem)

        self.buckets = new_buckets
        self.capacity = new_capacity

    def hash(self, x, capacity):
        x *= self.constant
        x -= int(x)
        x *= capacity

        return int(x)

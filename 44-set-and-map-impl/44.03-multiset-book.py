"""
A multiset is a set that allows multiple copies of the same element. Implement a Multiset class with the following methods:

- add(x): adds a 'copy' of x to the multiset.
- remove(x): removes a 'copy' of x from the multiset.
- contains(x): return whether x is in the multiset (at least one copy).
- size(): return the number of elements in the multiset (including copies).
"""


class HashMap:
    def __init__(self, h):
        self.h = h
        self.capacity = 10
        self._size = 0
        self.buckets = [[] for _ in range(self.capacity)]

    def size(self):
        return self._size

    def contains(self, k):
        hash = self.h(k, self.capacity)

        for key, _ in self.buckets[hash]:
            if key == k:
                return True

        return False

    def get(self, k):
        hash = self.h(k, self.capacity)

        for key, val in self.buckets[hash]:
            if key == k:
                return val

        return None

    def add(self, k, v):
        hash = self.h(k, self.capacity)

        for i, (key, _) in enumerate(self.buckets[hash]):
            if key == k:
                self.buckets[hash][i] = (k, v)
                return

        self.buckets[hash].append((k, v))
        self._size += 1

        load_factor = self._size / self.capacity

        if load_factor > 1:
            self.resize(self.capacity * 2)

    def remove(self, k):
        hash = self.h(k, self.capacity)

        for i, (key, _) in enumerate(self.buckets[hash]):
            if key == k:
                self.buckets[hash].pop(i)
                self._size -= 1
                load_factor = self._size / self.capacity

                if load_factor < 0.25 and self.capacity > 10:
                    self.resize(self.capacity // 2)

    def resize(self, new_capacity):
        new_buckets = [[] for _ in range(new_capacity)]

        for bucket in self.buckets:
            for k, v in bucket:
                hash = self.h(k, new_capacity)
                new_buckets[hash].append((k, v))

        self.buckets = new_buckets
        self.capacity = new_capacity


class MultiSet:
    # stores count, so instead of
    # buckets[hash] = [v1, v2, v3], it stores
    # buckets[hash] = [(v1, v1_count), (v2, v2_count), (v3, v3_count)]
    def __init__(self, h):
        self.map = HashMap(h)
        self._size = 0

    def size(self):
        return self._size

    def contains(self, x):
        return self.map.contains(x)

    def add(self, x):
        count = self.map.get(x)

        if count is None:
            self.map.add(x, 1)
        else:
            self.map.add(x, count + 1)

        self._size += 1

    def remove(self, x):
        count = self.map.get(x)

        if count is None:
            return

        if count == 1:
            self.map.remove(x)
        else:
            self.map.add(x, count - 1)

        self._size -= 1


def h_int(num, capacity):
    CONSTANT = 0.6180339887
    num *= CONSTANT
    num -= int(num)
    num *= capacity
    return int(num)


m = MultiSet(h_int)
assert m.size() == 0, f"\nsize(): got: {m.size()}, want: 0\n"
assert not m.contains(1), "\ncontains(1): got: true, want: false\n"

m.add(1)
assert m.size() == 1, f"\nsize(): got: {m.size()}, want: 1\n"
assert m.contains(1), "\ncontains(1): got: false, want: true\n"

# Test multiple copies
m.add(1)
assert m.size() == 2, f"\nsize(): got: {m.size()}, want: 2\n"
assert m.contains(1), "\ncontains(1): got: false, want: true\n"

# Test multiple elements
m.add(2)
m.add(3)
assert m.size() == 4, f"\nsize(): got: {m.size()}, want: 4\n"

# Test remove
m.remove(1)
assert m.size() == 3, f"\nsize(): got: {m.size()}, want: 3\n"
assert m.contains(1), "\ncontains(1): got: false, want: true\n"

m.remove(1)
assert m.size() == 2, f"\nsize(): got: {m.size()}, want: 2\n"
assert not m.contains(1), "\ncontains(1): got: true, want: false\n"

# Test remove non-existent
m.remove(4)
assert m.size() == 2, f"\nsize(): got: {m.size()}, want: 2\n"

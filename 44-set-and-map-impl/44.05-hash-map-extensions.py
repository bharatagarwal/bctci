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
    def __init__(self, h):
        self.h = h
        self.capacity = 10
        self._size = 0
        self.buckets = [[] for _ in range(self.capacity)]

    def keys(self):
        """
        returns a list of all keys

        T: amortised O(size) assuming good hash fn, and resizing
        S: amortised O(size) assuming good hash fn, and resizing
        """
        res = []

        for bucket in self.buckets:
            for k, _ in bucket:
                res.append(k)

        return res

    def values(self):
        """return a list of all values, repetitions should be included

        T: amortised O(size) assuming good hash fn, and resizing
        S: amortised O(size) assuming good hash fn, and resizing
        """

        res = []

        for bucket in self.buckets:
            for _, v in bucket:
                res.append(v)

        return res

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

        if self._load_factor() > 1:
            self._resize(self.capacity * 2)

    def remove(self, k):
        hash = self.h(k, self.capacity)

        for i, (key, _) in enumerate(self.buckets[hash]):
            if key == k:
                self.buckets[hash].pop(i)
                self._size -= 1

                if self._load_factor() < 0.25:
                    self._resize(self.capacity // 2)

    def _load_factor(self):
        return self._size / self.capacity

    def _resize(self, new_capacity):
        new_buckets = [[] for _ in range(new_capacity)]

        for bucket in self.buckets:
            for k, v in bucket:
                hash = self.h(k, new_capacity)
                new_buckets[hash].append((k, v))

        self.capacity = new_capacity
        self.buckets = new_buckets


def h_int(num, capacity):
    CONSTANT = 0.6180339887
    num *= CONSTANT
    num -= int(num)
    num *= capacity
    return int(num)


# Test basic operations
m = HashMap(h_int)
assert m.size() == 0, f"\nsize(): got: {m.size()}, want: 0\n"
assert not m.contains(1), "\ncontains(1): got: true, want: false\n"
assert m.get(1) == None, "\nget(1): got: not None, want: None\n"

m.add(1, "one")
assert m.size() == 1, f"\nsize(): got: {m.size()}, want: 1\n"
assert m.contains(1), "\ncontains(1): got: false, want: true\n"
assert m.get(1) == "one", f"\nget(1): got: {m.get(1)}, want: one\n"

# Test updating existing key
m.add(1, "ONE")
assert m.size() == 1, f"\nsize(): got: {m.size()}, want: 1\n"
assert m.get(1) == "ONE", f"\nget(1): got: {m.get(1)}, want: ONE\n"

# Test multiple elements
m.add(2, "two")
m.add(3, "three")
assert m.size() == 3, f"\nsize(): got: {m.size()}, want: 3\n"

# Test remove
m.remove(2)
assert m.size() == 2, f"\nsize(): got: {m.size()}, want: 2\n"
assert not m.contains(2), "\ncontains(2): got: true, want: false\n"
assert m.get(2) == None, "\nget(2): got: not None, want: None\n"

# Test resize up
m2 = HashMap(h_int)
for i in range(20):
    m2.add(i, str(i))
assert m2.size() == 20, f"\nsize(): got: {m2.size()}, want: 20\n"

# Test resize down
for i in range(15):
    m2.remove(i)
assert m2.size() == 5, f"\nsize(): got: {m2.size()}, want: 5\n"

# Test keys() and values()
m3 = HashMap(h_int)
m3.add(1, "one")
m3.add(2, "two")
m3.add(3, "three")

keys = m3.keys()
keys.sort()
assert keys == [1, 2, 3], f"\nkeys(): got: {keys}, want: [1, 2, 3]\n"

values = m3.values()
values.sort()
assert values == ["one", "three", "two"], (
    f"\nvalues(): got: {values}, want: ['one', 'three', 'two']\n"
)

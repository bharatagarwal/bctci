"""
# Multimap

A multimap is a map that allows multiple key-value pairs with the same key. Implement a multimap data structure with the following API:

- add(k, v): adds key k with value v to the multimap, even if key k is already found
- remove(k): removes all key-value pairs with k as the key
- contains(k): returns whether the multimap contains any key-value pair with k as the key
- get(k): returns all values associated to key k in a list.     If there is none, returns an empty list
- size(): returns the number of key-value pairs in the multimap

Constraints:

If your language is typed, you can either implement a multimap for integers, or make it generic.
The multimap will contain at most 10^6 key-value pairs.
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


class MultiMap:
    # essentially, value becomes an array of values instead of a single value
    # (k, [v1, v2, v3...])
    def __init__(self, h):
        self.map = HashMap(h)
        self._size = 0

    def size(self):
        return self._size

    def contains(self, k):
        return self.map.contains(k)

    def get(self, k):
        values = self.map.get(k)

        if values is None:
            return []

        return values

    def add(self, k, v):
        values = self.get(k)
        values.append(v)

        # replacing with array of tuples
        # buckets[hash] = (k, [v1, v2, v3....])
        self.map.add(k, values)

        self._size += 1

    def remove(self, k):
        if self.contains(k):
            self._size -= len(self.get(k))
            self.map.remove(k)


def h_int(num, capacity):
    CONSTANT = 0.6180339887
    num *= CONSTANT
    num -= int(num)
    num *= capacity
    return int(num)


# Test basic operations
m = MultiMap(h_int)
assert m.size() == 0, f"\nsize(): got: {m.size()}, want: 0\n"
assert not m.contains(1), "\ncontains(1): got: true, want: false\n"
assert m.get(1) == [], f"\nget(1): got: {m.get(1)}, want: []\n"

# Test add
m.add(1, "one")
assert m.size() == 1, f"\nsize(): got: {m.size()}, want: 1\n"
assert m.contains(1), "\ncontains(1): got: false, want: true\n"
assert m.get(1) == ["one"], (
    f"\nget(1): got: {m.get(1)}, want: ['one']\n"
)

# Test multiple values for same key
m.add(1, "ONE")
assert m.size() == 2, f"\nsize(): got: {m.size()}, want: 2\n"
assert m.get(1) == ["one", "ONE"], (
    f"\nget(1): got: {m.get(1)}, want: ['one', 'ONE']\n"
)

# Test multiple keys
m.add(2, "two")
assert m.size() == 3, f"\nsize(): got: {m.size()}, want: 3\n"
assert m.get(2) == ["two"], (
    f"\nget(2): got: {m.get(2)}, want: ['two']\n"
)

# Test remove
m.remove(1)
assert m.size() == 1, f"\nsize(): got: {m.size()}, want: 1\n"
assert not m.contains(1), "\ncontains(1): got: true, want: false\n"
assert m.get(1) == [], f"\nget(1): got: {m.get(1)}, want: []\n"

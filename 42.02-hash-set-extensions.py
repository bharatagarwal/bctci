class HashSet:
    constant = 0.6180339887

    def __init__(self):
        self.capacity = 10
        self._size = 0
        self.buckets = [[] for _ in range(self.capacity)]

    def add(self, x):
        h = self.hash(x, self.capacity)

        if x in self.buckets[h]:
            return True

        self.buckets[h].append(x)
        self._size += 1

        load_factor = self._size / self.capacity

        if load_factor > 1:
            self.resize(self.capacity * 2)

    def resize(self, new_capacity):
        new_buckets = [[] for _ in range(new_capacity)]

        for bucket in self.buckets:
            for elem in bucket:
                h = self.hash(elem, new_capacity)
                new_buckets[h].append(elem)

        self.buckets = new_buckets
        self.capacity = new_capacity

    def contains(self, x):
        h = self.hash(x, self.capacity)
        return x in self.buckets[h]

    def remove(self, x):
        h = self.hash(x, self.capacity)

        if x in self.buckets[h]:
            self.buckets[h].remove(x)
            self._size -= 1

            load_factor = self._size / self.capacity

            if load_factor < 0.25 and self.capacity > 10:
                self.resize(self.capacity // 2)

            return

    def size(self):
        return self._size

    def hash(self, x, capacity):
        x *= self.constant
        x -= int(x)
        x *= capacity

        return int(x)

    def elements(self):
        """returns all elements in a dynamic array"""
        res = list()

        for bucket in self.buckets:
            if bucket:
                res.extend(bucket)

        return res

    def union(self, s):
        """returns a new set that includes all the elements in either set"""
        res = HashSet()

        for el in self.elements():
            res.add(el)

        for el in s.elements():
            res.add(el)

        return res

    def intersection(self, s):
        """returns a new set that returns elements in both sets.

        if not common sets, return empty set.

        do not modify either set
        """
        res = HashSet()

        elements = self.elements()

        for el in elements:
            if s.contains(el):
                res.add(el)

        return res


h = HashSet()
h.add(12)

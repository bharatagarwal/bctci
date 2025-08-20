class HashSet:
    constant = 0.6180339887

    def __init__(self, size):
        self.members = [None] * size
        self.len = size

    def add(self, val):
        hashed = self.hash(val)

        if not self.members[hashed]:
            self.members[hashed] = [val]
        else:
            self.members[hashed].append(val)

    def contains(self, val):
        return self.members[self.hash(val)] is not None

    def remove(self, val):
        hashed = self.hash(val)
        if self.contains(val):
            if len(self.members[hashed]) == 1:
                self.members[hashed] = None
            else:
                self.members[self.hash(val)].remove(val)

    def size(self):
        return self.len

    def hash(self, val):
        val *= self.constant
        val -= int(val)
        val *= self.len

        return int(val)


h = HashSet(1000)
h.add(12)

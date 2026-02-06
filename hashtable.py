class HashTable:
    def __init__(self, size):
        self.data = [None] * size

    def _hash(self, key) -> int:
        """Private func don't invoke outside of the class."""
        hash = 0
        for idx in range(0, len(key)):
            hash = (hash + ord(key[idx]) * idx) % len(self.data)
        return hash

    def set(self, key, value):
        address = self._hash(key)

        # handle key collisions, if at same address 
        # just append to existing array on that address
        if (not self.data[address]):
            self.data[address] = []
        self.data[address].append([key, value])
        return self.data

    def get(self, key):
        address = self._hash(key)
        current = self.data[address]
        if (len(current) > 0):
            for i in range(0, len(current)):
                if(current[i][0] == key):
                    return current[i][1]
        return None

    def get_all(self):
        for i in range(0, len(self.data)):
            if self.data[i] is not None:
                print(self.data[i])

hashtable = HashTable(2)
hashtable.set('hello', 1000)
hashtable.set('world', 2000)
# print(hashtable.get())
print(hashtable.get('hello'))
# print(hashtable.get('world'))
# hashtable.get_all()
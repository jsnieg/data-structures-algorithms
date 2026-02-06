class HashTable:
    
    def __init__(self, size):
        self.data = [None] * size


    def _hash(self, key) -> int:
        """Private func don't invoke outside of the class."""
        hash = 0
        for idx in range(0, len(key)):
            hash = (hash + ord(key[idx]) * idx) % len(self.data)
        return hash


    def set(self, key, value) -> list:
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


    def keys(self) -> list:
        keys = []
        for i in range(0, len(self.data)):
            if (self.data[i] is not None):
                keys.append(self.data[i][0][0])
        return keys


hashtable = HashTable(50)
hashtable.set('grapes', 1000)
hashtable.set('bananas', 2000)
hashtable.set('pears', 4000)
hashtable.set('apples', 1500)
print(hashtable.get('bananas'))
print(hashtable.keys())
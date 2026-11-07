# Hash table

```puthon
class HashTable:
    def __init__(self):
        self.collection = {}

    def hash(self, string: str) -> int:
        return sum(ord(ch) for ch in string)

    def add(self, key: str, val: str) -> None:
        hash_key = self.hash(key)

        if hash_key not in self.collection:
            self.collection[hash_key] = {}

        self.collection[hash_key][key] = val

    def remove(self, key: str) -> None:
        hash_key = self.hash(key)

        if hash_key in self.collection:
            if key in self.collection[hash_key]:
                del self.collection[hash_key][key]

    def lookup(self, key: str) -> None:
        hash_key = self.hash(key)

        if hash_key in self.collection:
            return self.collection[hash_key].get(key) 

        return None

    def __str__(self):
        return f'{self.collection}'

h = HashTable()
print(h)
h.add("3", "4")
h.add("3", "5")
h.add("5", "6")
h.add("fcc", "fgf")

print(h)

h.remove("5")
print(h)

print(h.lookup("cfc"))
```

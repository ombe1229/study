from open_addressing import OpenHash


hash = OpenHash(13)
hash.add(1, "a")
hash.add(5, "b")
hash.add(6, "c")
hash.add(8, "d")
hash.add(10, "e")
hash.add(19, "f")
hash.dump()
print("----------")
hash.remove(8)
hash.dump()
print("----------")
print(hash.search(19))

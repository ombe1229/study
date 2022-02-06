input()
l = input()
r = 0
for n, t in enumerate(l):
    r += (ord(t) - 96) * 31 ** n
print(r % 1234567891)

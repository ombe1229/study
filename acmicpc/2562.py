l = []
for _ in range(9):
    l.append(int(input()))
m = max(l)
print(m)
print(l.index(m) + 1)

l = []
for _ in range(10):
    l.append(int(input()) % 42)
print(len(set(l)))

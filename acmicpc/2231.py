n = int(input())
for i in range(1, n + 1):
    s = sum(map(int, str(i)))
    if i + s == n:
        print(i)
        break
else:
    print(0)

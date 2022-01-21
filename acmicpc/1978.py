input()
l = list(map(int, input().split()))

m = max(l)
arr = [True for _ in range(m + 1)]
arr[0] = False
arr[1] = False

for i in range(2, int(m ** (1 / 2)) + 1):
    if arr[i]:
        j = 2
        while i * j <= m:
            arr[i * j] = False
            j += 1

ret = 0
for i in l:
    if arr[i]:
        ret += 1
print(ret)

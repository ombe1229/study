from math import sqrt, ceil


n = int(input())
m = ceil(sqrt(n + 1)) * 2
s = [True] * m

for i in range(2, int(sqrt(m)) + 1):
    if s[i]:
        for j in range(i * 2, m, i):
            s[j] = False

arr = [i for i in range(2, m) if s[i]]

for i in range(len(arr) - 1):
    if arr[i] * arr[i + 1] > n:
        print(arr[i] * arr[i + 1])
        break

from sys import stdin

input = stdin.readline

for _ in range(int(input())):
    h, w, n = map(int, input().split())
    if n % h == 0:
        ret = h * 100 + n // h
    else:
        ret = n % h * 100 + n // h + 1
    print(ret)

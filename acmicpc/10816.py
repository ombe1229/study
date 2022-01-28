from collections import Counter
from sys import stdin

input = stdin.readline

input()
l = map(int, input().split())
input()
ll = map(int, input().split())

c = Counter(l)
print(*[c[n] if n in c else 0 for n in ll])

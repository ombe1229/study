from sys import stdin
from collections import deque

input = stdin.readline

n = int(input())
l = deque([n])

for i in range(n - 1, 0, -1):
    l.appendleft(i)
    for j in range(i):
        l.appendleft(l.pop())

print(*l)

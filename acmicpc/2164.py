from sys import stdin
from collections import deque

input = stdin.readline

n = int(input())
l = deque(list(range(1, n + 1)))

while len(l) > 1:
    l.popleft()
    l.append(l.popleft())

print(l[0])

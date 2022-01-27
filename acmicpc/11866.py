from collections import deque
from sys import stdin

input = stdin.readline

n, k = map(int, input().split())
l = deque(range(1, n + 1))
ret = []

while l:
    for _ in range(k - 1):
        l.append(l.popleft())
    ret.append(l.popleft())

print(f"<{', '.join(map(str, ret))}>")

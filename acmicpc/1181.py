from sys import stdin

input = stdin.readline
l = set()
for _ in range(int(input())):
    l.add(input().rstrip())
l = list(l)
l.sort()
l.sort(key=len)
print(*l, sep="\n")

from sys import stdin

input = stdin.readline

l = []
for _ in range(int(input())):
    l.append(tuple(map(int, input().split())))
l.sort(key=lambda x: (x[1], x[0]))
for i in l:
    print(i[0], i[1])

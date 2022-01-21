from sys import stdin

input = stdin.readline

l = [0] * 10001
for _ in range(int(input())):
    l[int(input())] += 1

for i in range(10001):
    if l[i] != 0:
        for j in range(l[i]):
            print(i)

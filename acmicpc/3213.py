from sys import stdin

input = stdin.readline

d = [0, 0, 0]
"""
d[0]: 1/4조각 먹는 사람
d[1]: 1/2조각 먹는 사람
d[2]: 3/4조각 먹는 사람
"""
pizza = 0

for _ in range(int(input())):
    t = input().strip()
    if t == "1/4":
        d[0] += 1
    elif t == "1/2":
        d[1] += 1
    else:
        d[2] += 1

if d[1] % 2 == 0:
    pizza += d[1] // 2
    d[1] = 0
elif d[1] % 2 == 1 and d[1] != 1:
    pizza += d[1] // 2
    d[1] = 1


if min(d[0], d[2]) != 0:
    g = min(d[0], d[2])
    pizza += g
    d[0] -= g
    d[2] -= g

if d[0] >= 4:
    pizza += d[0] // 4
    d[0] %= 4

if d[0] >= 1 and d[1] == 1:
    pizza += 1
    d[0] -= 2
    d[1] = 0

if d[0] >= 1:
    pizza += 1

if d[1] >= 1:
    pizza += 1

if d[2] >= 1:
    pizza += d[2]

print(int(pizza))

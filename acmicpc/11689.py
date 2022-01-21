from sys import stdin

input = stdin.readline
n = int(input())

t = 2
ret = n
while t ** 2 <= n:
    if n % t == 0:
        ret -= ret / t
        while n % t == 0:
            n /= t
    t += 1
if n > 1:
    ret -= ret / n

print(int(ret))

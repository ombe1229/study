from math import factorial, gcd
from sys import stdin

for _ in range(5):
    n, k = map(int, stdin.readline().split())
    print(gcd(factorial(n), k))

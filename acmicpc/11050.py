from sys import stdin
from math import factorial

input = stdin.readline


n, k = map(int, input().split())
print(factorial(n) // (factorial(k) * factorial(n - k)))

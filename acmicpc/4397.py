from math import comb
from sys import stdin


for line in stdin.readlines():
    p, q, r, s = map(int, line.split())
    print(f"{comb(p, q) / comb(r, s):.5f}")

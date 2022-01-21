from itertools import combinations
from sys import stdin

input = stdin.readline

m = int(input().split()[1])
l = map(int, input().split())
print(max(filter(lambda x: x <= m, {sum(i) for i in combinations(l, 3)})))

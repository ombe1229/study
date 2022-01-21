from sys import stdin

input = stdin.readline

input()
a = set(map(int, input().split()))
input()
b = map(int, input().split())
for i in b:
    print(int(i in a))

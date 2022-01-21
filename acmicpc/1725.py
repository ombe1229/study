from sys import stdin

input = stdin.readline

n = int(input())
l = [int(input()) for _ in range(n)]
stack = []
value = 0

for i in range(n):
    while stack and l[stack[-1]] > l[i]:
        h = l[stack[-1]]
        stack.pop()
        w = i
        if stack:
            w = i - stack[-1] - 1
        value = max(value, w * h)
    stack.append(i)

while stack:
    h = l[stack[-1]]
    stack.pop()
    w = n
    if stack:
        w = n - stack[-1] - 1
    value = max(value, w * h)

print(value)

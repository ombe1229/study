from collections import deque
from sys import stdin

input = stdin.readline

d = deque()

for _ in range(int(input())):
    command = input().strip()
    if command.startswith("push"):
        d.append(command.split()[1])
    elif command == "pop":
        print(d.popleft() if d else -1)
    elif command == "size":
        print(len(d))
    elif command == "empty":
        print(int(not d))
    elif command == "front":
        print(d[0] if d else -1)
    elif command == "back":
        print(d[-1] if d else -1)

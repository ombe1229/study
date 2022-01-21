from sys import stdin

sr = stdin.readline

l = []

for _ in range(int(sr().strip())):
    command = sr().strip()
    if command.startswith("push"):
        l.append(command.split()[1])
    elif command == "pop":
        print(l.pop(-1) if l else -1)
    elif command == "size":
        print(len(l))
    elif command == "empty":
        print(int(not l))
    elif command == "top":
        print(l[-1] if l else -1)

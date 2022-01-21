from sys import stdin

input = stdin.readline

for _ in range(int(input())):
    text = input()
    t = 0
    for i in text:
        if i == "(":
            t += 1
        elif i == ")":
            t -= 1
        if t == -1:
            break
    if t == 0:
        print("YES")
    else:
        print("NO")

for i in range(int(input())):
    x1, y1, r1, x2, y2, r2 = map(int, input().split())

    d = (((x1 - x2) ** 2 + (y1 - y2) ** 2)) ** 0.5
    a = r1 + r2
    s = abs(r1 - r2)

    if d == 0:
        if r1 == r2:
            print(-1)
        else:
            print(0)
    else:
        if d < a and d > s:
            print(2)
        elif d == a or d == s:
            print(1)
        else:
            print(0)

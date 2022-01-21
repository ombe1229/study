for _ in range(int(input())):
    r, s = input().split()
    r = int(r)
    for i in s:
        print(i * r, end="")
    print("")

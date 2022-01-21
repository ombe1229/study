while 1:
    t = input()
    if t == "0":
        break
    print("yes" if t == t[::-1] else "no")

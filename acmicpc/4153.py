while 1:
    a = list(map(int, input().split()))
    max_num = max(a)
    if sum(a) == 0:
        break
    a.remove(max_num)
    print("right" if a[0] ** 2 + a[1] ** 2 == max_num ** 2 else "wrong")

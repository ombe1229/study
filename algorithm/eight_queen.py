"""branching and bounding method"""

pos = [0] * 8
row = [False] * 8
dia_r = [False] * 15
dia_l = [False] * 15


def put() -> None:
    for i in range(8):
        print(f"{pos[i]:2}", end="")
    print()


def set(i: int) -> None:
    for j in range(8):
        if not row[j] and not dia_r[i + j] and not dia_l[i - j + 7]:
            pos[i] = j
            if i == 7:
                put()
            else:
                row[j] = dia_r[i + j] = dia_l[i - j + 7] = True
                set(i + 1)
                row[j] = dia_r[i + j] = dia_l[i - j + 7] = False


set(0)

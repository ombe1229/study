from functools import cmp_to_key


def cmp(a, b):
    if a > b:
        return 1
    elif a < b:
        return -1
    else:
        return 0


l = [1, 4, 3, 2, 5]
sorted_list = sorted(l, key=cmp_to_key(cmp))
print(sorted_list)

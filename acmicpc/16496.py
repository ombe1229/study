from functools import cmp_to_key


input()
l = input().split()
l.sort(key=cmp_to_key(lambda x, y: -1 if int(x + y) > int(y + x) else 1))
print(0 if sum(map(int, l)) == 0 else "".join(l))

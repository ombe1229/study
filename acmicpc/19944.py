n, m = map(int, input().split())
if m in [1, 2]:
    r = "NEWBIE!"
elif m <= n:
    r = "OLDBIE!"
else:
    r = "TLE!"
print(r)

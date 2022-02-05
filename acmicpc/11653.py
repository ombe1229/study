n = int(input())
t = 2
while n > 1:
    if not n % t:
        n /= t
        print(t)
    else:
        t += 1

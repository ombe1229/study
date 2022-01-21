n = int(input())

count = 0
while n >= 0:
    if n % 5 == 0:
        print(count + n // 5)
        break
    n -= 3
    count += 1
else:
    print(-1)

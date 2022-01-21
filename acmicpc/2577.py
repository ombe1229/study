x = 1

for _ in range(3):
    x *= int(input())

for i in range(10):
    print(int(str(x).count(str(i))))

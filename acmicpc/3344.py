# https://en.wikipedia.org/wiki/Eight_queens_puzzle#Existence_of_solutions

n = int(input())
m = n // 2 + 1

if n % 6 not in [2, 3]:
    for i in range(1, m):
        print(i * 2 - 1)
    if n % 2:
        print(n)
    for i in range(1, m):
        print(i * 2)
elif n % 6 == 2:
    for i in range(1, m):
        print(i * 2)
    print("3\n1")
    for i in range(3, m - 1):
        print(i * 2 + 1)
    print(5)
elif n % 6 == 3:
    for i in range(2, m):
        print(i * 2)
    print(2)
    for i in range(2, m):
        print(i * 2 + 1)
    print("1\n3")

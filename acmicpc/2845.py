l, p = map(int, input().split())
a = map(int, input().split())
b = l * p
for i in a:
    print(i - b, end=" ")

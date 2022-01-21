zero = [1, 0, 1]
one = [0, 1, 1]


def fibo():
    n = int(input())
    if n >= len(zero):
        for i in range(len(zero), n + 1):
            zero.append(zero[i - 2] + zero[i - 1])
            one.append(one[i - 2] + one[i - 1])
    print(zero[n], one[n])


for _ in range(int(input())):
    fibo()

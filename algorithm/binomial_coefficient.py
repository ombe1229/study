def bino(n, r):
    if r > n:
        return 0
    if r == 0 or r == n:
        return 1

    return bino(n - 1, r - 1) + bino(n - 1, r)

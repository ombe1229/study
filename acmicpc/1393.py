x_s, y_s = map(int, input().split())
x_e, y_e, d_x, d_y = map(int, input().split())


def get_m(x, y):
    if x < y:
        x, y = y, x
    while y > 0:
        x, y = y, x % y
    return x


m = get_m(d_x, d_y)
d_x /= m
d_y /= m
f_x, f_y = x_e, y_e

while 1:
    d = ((x_s - f_x) ** 2 + (y_s - f_y) ** 2) ** (1 / 2)
    if d < (((x_s - x_e) ** 2) + ((y_s - y_e) ** 2)) ** (1 / 2):
        print(int(f_x), int(f_y))
        break
    f_x, f_y = x_e, y_e
    x_e += d_x
    y_e += d_y

# https://en.wikipedia.org/wiki/Linear_congruential_generator


from typing import Generator


def lcg(
    modulus: int, a: int, c: int, seed: int, loop: int
) -> Generator[int, None, None]:
    for _ in range(loop):
        seed = (a * seed + c) % modulus
        yield seed


l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for i, j in enumerate(lcg(2 ** 31, 1103515245, 12345, len(l), len(l))):
    j %= len(l)
    l[i], l[j] = l[j], l[i]
print(l)

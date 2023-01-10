from sys import stdin


input = stdin.readline


def get_key(word):
    t = list(word)
    key = (t.pop(0), t.pop(-1))
    t.sort()
    return (tuple(t), key)


d = {}
for _ in range(int(input())):
    word = input().strip()
    if len(word) > 2:
        d[get_key(word)] = word

input()
s = input().strip().split()
result = []
for i in s:
    if len(i) > 2:
        result.append(d[get_key(i)])
    else:
        result.append(i)

print(" ".join(result))

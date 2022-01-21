l = int(input())
t = input()

pi = [0] * l
j = 0
for i in range(1, l):
    while j > 0 and t[i] != t[j]:
        j = pi[j - 1]
    if t[i] == t[j]:
        j += 1
        pi[i] = j

print(l - pi[-1])

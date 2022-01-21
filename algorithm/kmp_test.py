from kmp import kmp_match

s1 = input("txt: ")
s2 = input("pattern: ")

idx = kmp_match(s1, s2)

if idx == -1:
    print("nn")
else:
    print(idx + 1)

def check(w):
    for i in range(len(w) - 1):
        if w.find(w[i]) > w.find(w[i + 1]):
            return False
    return True


count = 0
for _ in range(int(input())):
    if check(input()):
        count += 1
print(count)

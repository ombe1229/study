for _ in range(int(input())):
    score, cont = 0, 0
    for i in input():
        if i == "O":
            cont += 1
            score += cont
        else:
            cont = 0
    print(score)

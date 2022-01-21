def get_pi(pat):
    l = len(pat)
    pi = [0] * l
    j = 0
    for i in range(l):
        while j > 0 and pat[i] != pat[j]:
            j = pi[j - 1]
        if pat[i] == pat[j]:
            j += 1
            pi[i] = j

    return pi

def kmp_match(txt: str, pattern: str) -> int:
    pt = 1
    pp = 0
    skip = [0] * (len(pattern) + 1)

    skip[pt] = 0
    while pt != len(pattern):
        if pattern[pt] == pattern[pp]:
            pt += 1
            pp += 1
            skip[pt] = pp
        elif pp == 0:
            pt += 1
            skip[pt] = pp
        else:
            pp = skip[pp]

    pt = pp = 0
    while pt != len(txt) and pp != len(pattern):
        if txt[pt] == pattern[pp]:
            pt += 1
            pp += 1
        elif pp == 0:
            pt += 1
        else:
            pp = skip[pp]

    return pt - pp if pp == len(pattern) else -1

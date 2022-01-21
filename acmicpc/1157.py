from collections import Counter

c = Counter(input().upper())
most = c.most_common(2)
print(most[0][0] if len(most) == 1 or most[0][1] != most[1][1] else "?")

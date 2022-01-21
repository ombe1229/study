n, l, k = map(int, input().split())
easy, hard = 0, 0
score = 0

for i in range(n):
    sub1, sub2 = map(int, input().split())
    if sub2 <= l:
        hard += 1
    elif sub1 <= l:
        easy += 1

if hard > k:
    score = k * 140
else:
    score = hard * 140
    k -= hard
    if easy > k:
        score += k * 100
    else:
        score += easy * 100

print(score)

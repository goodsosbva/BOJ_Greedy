n = int(input())

sequence = []
negative = []
positive = []
res = 0
for i in range(n):
    i = int(input())
    sequence.append(i)

for k in sequence:
    if k < 0:
        negative.append(k)
    elif k > 0:
        positive.append(k)
    else:
        negative.append(k)

negative.sort()
positive.sort(reverse=True)
# print(negative)
u = len(negative)
if 0 in negative:
    if u % 2 == 0:
        for q in range(0, u, 2):
            res += negative[q] * negative[q + 1]
    else:
        for w in range(0, u - 1, 2):
            res += negative[w] * negative[w + 1]
else:
    if u % 2 == 0:
        for q in range(0, u, 2):
            res += negative[q] * negative[q + 1]
    elif u % 2 != 0 and u != 1:
        for w in range(0, u - 1, 2):
            res += negative[w] * negative[w + 1]
        res += negative[u - 1]
    else:
        res += negative[0]
# print("음수합:", res)
# print(positive)
v = len(positive)
if 1 in positive:
    x = positive.count(1)
    # print(x)
    if v - 1 > x:
        if v % 2 == 0:
            for s in range(0, v - x, 2):
                res += positive[s] * positive[s + 1]
            res += x
        else:
            for t in range(0, v - x, 2):
                res += positive[t] * positive[t + 1]
            res += x
    else:
        for h in positive:
            res += h
else:
    if v % 2 == 0:
        for r in range(0, v, 2):
            res += positive[r] * positive[r + 1]

    else:
        for f in range(0, v - 1, 2):
            res += positive[f] * positive[f + 1]
        res += positive[v - 1]

print(res)

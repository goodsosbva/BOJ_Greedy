n, k = map(int, input().split())

coins = []
res = 0
cnt = 0

for i in range(n):
    i = int(input())
    coins.append(i)

coins.reverse()

for c in coins:
    if k // c == 0:
        continue
    else:
        cnt = k // c
        res += cnt
        k = k - (cnt * c)
        if k == 0:
            break
print(res)
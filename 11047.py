n, k = map(int, input().split())

coins = []
sum = 0
cnt = 0

for i in range(n):
    i = int(input())
    coins.append(i)

# print(coins)

for j in range(n):
    if k < coins[j + 1]:
        sum += coins[j]
        cnt += 1
        startnum = j
        break
    elif k == coins[j + 1]:
        sum += coins[j + 1]
        startnum = j
        cnt += 1
        break


# print(startnum)

while sum != k:
    if sum < k:
        sum += coins[startnum]
        cnt += 1
    elif sum == k:
        # sum += coins[startnum]
        cnt += 1
        break
    elif sum > k:
        sum -= coins[startnum]
        cnt -= 1
        startnum -= 1

# print(sum)
print(cnt)



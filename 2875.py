n, m, k = map(int, input().split())

res = 0
while True:
    if k == 0: break
    if n - 2 >= 0 and m - 1 >= 0:
        n -= 2
        m -= 1
        res += 1
        print(res)
    elif n - 1 >= 0:
        n -= 1
        k -= 1
        # if k == 0: break
    elif m - 1 >= 0:
        m -= 1
        k -= 1
        # if k == 0: break
    else:  # n - 1 < 0 and m - 1 < 0
        res -= 1
        n += 2
        m += 1
        if n - 1 >= 0:
            n -= 1
            k -= 1
        elif m - 1 >= 0:
            m -= 1
            k -= 1
print(res)

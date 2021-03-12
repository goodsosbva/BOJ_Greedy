n, m = map(int, input().split())


if n == 1:
    print(1)
elif n == 2:
    k = int((m + 1) // 2)
    print(min(k, 4))
elif m < 7:
    print(min(4, m))
else:
    print(m-7 + 5)
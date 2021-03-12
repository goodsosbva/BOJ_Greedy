# 동전과 값 입력받기
n, k = map(int, input().split())
# 동전을 입력받을 리스트 초기화하기
coin = []

# 동전 종류 입력받기
for i in range(n):
    coin.append(int(input()))

# 동전개수 셀 변수 초기화
result = 0

# 동전 내림차순으로 정렬하기
coin.sort(reverse=True)

# 동전 개수 구하기
for i in coin:
    if k == 0:
        break
    result += k // i
    k %= i
    print(k)

print(result)

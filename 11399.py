n = int(input())

sum = 0

lines = list(map(int, input().split(" ")))
# print(lines)
lines.sort()
# print(lines)

for l in range(len(lines)):
    for r in range(0, l + 1):
        sum += lines[r]

print(sum)

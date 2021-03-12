n = int(input())
Plans = []
for _ in range(n):
    Plans.append(list(map(int, input().split())))

# print(Plans)

plan = sorted(Plans, key=lambda x: (x[1], x[0]))

# print(plan)

end, res = 0, 0
for time in plan:
    if time[0] >= end:
        end = time[1]
        res += 1

print(res)

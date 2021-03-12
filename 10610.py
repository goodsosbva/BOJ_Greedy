n = (input())
n_int = int(n)
integers = []
sum = 0
for i in n:
    integers.append(i)

integers.sort()
# print(integers)
if n_int % 30 == 0:
    print(n_int)
elif integers[0] == '0':
    #print("elif")
    for i in range(1, len(integers)):
        sum += int(integers[i])
        # print(integers[i])
    #print(sum)
    if sum % 3 == 0:
        integers.sort(reverse=True)
        print(''.join(integers))
    else:
        print(-1)
else:
    print(-1)


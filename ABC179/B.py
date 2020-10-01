N = int(input())
flag = 0
cnt = 0

for _ in range(N):
    d1, d2 = map(int, input().split())
    # print(d1, d2)
    if d1 == d2:
        cnt += 1
    else:
        cnt = 0

    if cnt == 3:
        flag = 1

if flag == 1:
    print("Yes")
else:
    print("No")
# print(d1, d2)

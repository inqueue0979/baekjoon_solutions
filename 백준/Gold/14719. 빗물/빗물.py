from sys import stdin

H, W = map(int, stdin.readline().rstrip().split())
rain = [[0 for i in range(H)] for j in range(W)]
rain_list = list(map(int, stdin.readline().rstrip().split()))
ans = 0

for i in range(W):
    for j in range(rain_list[i]):
        rain[i][j] = 1

for h in range(H):
    temp = 0
    started = False
    for w in range(W):
        data = rain[w][h]
        if data == 1 and started == False:
            started = True
        elif data == 0 and started == True:
            temp += 1
        elif data == 1 and started == True:
            ans += temp
            temp = 0

print(ans)
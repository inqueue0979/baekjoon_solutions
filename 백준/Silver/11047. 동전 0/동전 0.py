from sys import stdin

N, K = map(int, stdin.readline().rstrip().split())
coins = sorted([int(stdin.readline().rstrip()) for i in range(N)], reverse=True)
answer = 0

for coin in coins:
    
    if K >= coin:
        answer += K // coin
        K %= coin

print(answer)
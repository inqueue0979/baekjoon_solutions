import sys

N, M = map(int, sys.stdin.readline().rstrip().split())
basket = [[0] for i in range(N)]

for _ in range(M):
    i, j, k = map(int, sys.stdin.readline().rstrip().split())

    for n in range(i - 1, j):
        basket[n][0] = k

for m in range(N):
    print(basket[m][-1], end=' ')
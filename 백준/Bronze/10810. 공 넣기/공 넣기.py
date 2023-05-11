import sys

N, M = map(int, sys.stdin.readline().rstrip().split())
basket = []

for _ in range(N):
    basket.append([])

for _ in range(M):
    i, j, k = map(int, sys.stdin.readline().rstrip().split())

    for n in range(i - 1, j):
        basket[n].append(k)

for m in range(N):
    if len(basket[m]) != 0:
        print(basket[m][-1], end=' ')
    else:
        print(0, end=' ')
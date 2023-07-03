from sys import stdin

N, M = map(int, stdin.readline().rstrip().split())
nums = list(map(int, stdin.readline().rstrip().split()))
prefix_sum = [nums[0]]

for i in range(1,N):
    prefix_sum.append(prefix_sum[i-1] + nums[i])

for _ in range(M):
    a, b = map(int, stdin.readline().rstrip().split())
    if a != 1:
        print(prefix_sum[b - 1] - prefix_sum[a - 2])
    else:
        print(prefix_sum[b - 1])
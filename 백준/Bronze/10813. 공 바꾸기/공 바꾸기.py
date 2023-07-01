from sys import stdin

N, M = map(int, stdin.readline().rstrip().split())
nums = [(i+1) for i in range(N)]

for _ in range(M):
    i, j = map(int, stdin.readline().rstrip().split())
    nums[i-1], nums[j-1] = nums[j-1], nums[i-1]

print(*nums)
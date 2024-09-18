from sys import stdin
nums = int(stdin.readline().rstrip())
sizes = list(map(int, stdin.readline().split()))
T, P = map(int, stdin.readline().split())
ans = 0

for i in sizes:
    ans += ((i - 1) // T) + 1;
print(ans)
print(nums // P, nums % P)
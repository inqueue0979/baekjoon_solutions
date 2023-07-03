from sys import stdin

N, S = map(int, stdin.readline().rstrip().split())
nums = list(map(int, stdin.readline().rstrip().split()))

answer = 100000001
start, end = 0, 0
sum = 0

while True:

    if sum >= S:
        answer = min(answer, end - start)
        sum -= nums[start]
        start += 1

    elif end == N:
        break

    else:
        sum += nums[end]
        end += 1

if answer == 100000001:
    answer = 0

print(answer)
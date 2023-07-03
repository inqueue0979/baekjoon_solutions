from sys import stdin

N, M = map(int, stdin.readline().rstrip().split())
nums = list(map(int, stdin.readline().rstrip().split()))

answer = 0
start, end = 0, 1

while end <= N:

    sums = sum(nums[start:end])
    
    if sums == M:
        answer += 1
        start += 1
    elif sums > M:
        start += 1
    else:
        end += 1

print(answer)
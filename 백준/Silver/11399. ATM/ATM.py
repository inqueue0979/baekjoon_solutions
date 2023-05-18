from sys import stdin

N = int(stdin.readline().rstrip())
time = sorted(map(int, stdin.readline().rstrip().split()))
answer = 0

for i in time:
    answer += i * N
    N -= 1

print(answer)
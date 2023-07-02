from sys import stdin

count = int(stdin.readline().rstrip())
A = sorted(list(map(int, stdin.readline().rstrip().split())), reverse=True)
B = sorted(list(map(int, stdin.readline().rstrip().split())))
answer = 0

for i in range(count):
    answer += A[i] * B[i]

print(answer)
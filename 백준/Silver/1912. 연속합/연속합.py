from sys import stdin

cases = int(stdin.readline().rstrip())
data = list(map(int, stdin.readline().rstrip().split()))

for i in range(1, cases):
    data[i] = max(data[i], data[i] + data[i-1])

print(max(data))
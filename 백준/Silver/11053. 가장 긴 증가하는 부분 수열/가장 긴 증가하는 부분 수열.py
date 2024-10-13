from sys import stdin

length = int(stdin.readline().rstrip())
data = list(map(int, stdin.readline().rstrip().split()))
memo = list(1 for _ in range(length))

for i in range(1, length):
    temp = 1    
    for j in range(i):
        if data[i] > data[j]:
            memo[i] = max(memo[i], memo[j] + 1)
    
print(max(memo))
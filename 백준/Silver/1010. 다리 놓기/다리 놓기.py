import math

for i in range(int(input())):
    n, m = map(int, input().split())
    print(int(math.factorial(m) / (math.factorial(m-n) * math.factorial(n))))
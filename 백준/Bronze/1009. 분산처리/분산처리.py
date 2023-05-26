from sys import stdin
for _ in range(int(stdin.readline().rstrip())):
    a, b = map(int, stdin.readline().rstrip().split())
    c = ((a ** (((b - 1) % 4) + 1))) % 10
    print(c) if c != 0 else print(10)
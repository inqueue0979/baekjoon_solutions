from sys import stdin

L, P = map(int, stdin.readline().rstrip().split())
L *= P
a = list(map(int, stdin.readline().rstrip().split()))

for i in a:
    print(i - L, end=' ')
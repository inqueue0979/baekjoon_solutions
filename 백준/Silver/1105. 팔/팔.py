from sys import stdin

ans = 0
L, R = map(str, stdin.readline().rstrip().split())
if len(L) == len(R):
    for i in range(len(L)):
        if L[i] == R[i] == '8':
            ans += 1
        elif L[i] != R[i]:
            break
    print(ans)
else:
    print(0)
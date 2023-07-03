from sys import stdin
from itertools import permutations

N = int(stdin.readline().rstrip())
M = int(stdin.readline().rstrip())
S = stdin.readline().rstrip()
answer = 0
IOI = 'IO' * N + "I"

for i in range(M - (2 * N)):
    if S[i:i+(2 * N + 1)] == IOI:
        answer += 1

print(answer)
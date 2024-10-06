from sys import stdin

S = list(stdin.readline().rstrip())
T = list(stdin.readline().rstrip())

while len(S) != len(T):

    if T[-1] == 'B':
        T.pop()
        T.reverse()
    else:
        T.pop()

if S == T:
    print(1)
else:
    print(0)
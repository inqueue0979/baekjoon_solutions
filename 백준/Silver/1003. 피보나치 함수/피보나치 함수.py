def fib(i, zero_one):

    if i > 2 and not zero_one.get(i, False):
        a = fib(i-1, zero_one)
        b = fib(i-2, zero_one)
        zero_one[i] = [a[0] + b[0], a[1] + b[1]]
    
    return zero_one[i]

from sys import setrecursionlimit, stdin
setrecursionlimit(100000)

for _ in range(int(stdin.readline().rstrip())):

    zero_one = {0:[1,0],
                1:[0,1],
                2:[1,1]}

    print(*fib(int(stdin.readline().rstrip()), zero_one))
def fib(num, memo):
    
    if memo.get(num):
        return memo[num]
    else:
        memo[num] = fib(num-1, memo) + fib(num-2, memo)
        return memo[num]

from sys import stdin, setrecursionlimit
setrecursionlimit(100000)

num = int(stdin.readline().rstrip())
memo = {
    0:1,
    1:1
}

print(fib(num, memo) % 10007)

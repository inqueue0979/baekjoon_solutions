def fibonacci(i, memo):
    
    if i > 2 and not memo.get(i, False):
        memo[i] = fibonacci(i-1, memo) + fibonacci(i-2, memo)

    return memo[i]

from sys import stdin
memo = {1:1,
        2:1}

print(fibonacci(int(stdin.readline().rstrip()), memo))
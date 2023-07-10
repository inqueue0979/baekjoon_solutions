from sys import stdin

dp = {1:0}

def func(a):
    
    if a in dp.keys():
        return dp[a]
    elif a % 2 == 0 and a % 3 == 0:
        dp[a] = min(func(a // 3) + 1, func(a // 2) + 1)
    elif a % 3 == 0:
        dp[a] = min(func(a // 3) + 1, func(a - 1) + 1)
    elif a % 2 == 0:
        dp[a] = min(func(a // 2) + 1, func(a - 1) + 1)
    else:
        dp[a] = func(a - 1) + 1
    
    return dp[a]

a = int(stdin.readline().rstrip())

print(func(a))
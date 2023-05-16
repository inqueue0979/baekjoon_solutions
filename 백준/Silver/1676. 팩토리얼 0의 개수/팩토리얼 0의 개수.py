from sys import stdin
answer = 0

def factorial(n):
    num = 1
    for i in range(1, n+1):
        num *= i
    return num

a = reversed(str(factorial(int(stdin.readline().rstrip()))))

for i in a:
    if i != '0':
        break
    
    answer += 1

print(answer)
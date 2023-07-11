import sys

def primes(n):
    numlist = [i for i in range(0, n + 1)]
    primelist = []
    numlist[1] = 0

    for i in range(0, n + 1):
        if numlist[i] == 0: continue
        
        for j in range(i * 2,n + 1, i):
            numlist[j] = 0

    for i in range(2, n + 1):
        if numlist[i] != 0: 
            primelist.append(i)

    return primelist

num = int(sys.stdin.readline().rstrip())
primelist = primes(num)

for i in primelist:
    while True:
        if num % i == 0:
            print(i)
            num = num // i
        else:
            break
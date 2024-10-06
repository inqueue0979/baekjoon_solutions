from sys import stdin

t = int(stdin.readline().rstrip())
while(t):
    t -= 1
    days = int(stdin.readline().rstrip())
    prices = list(map(int, stdin.readline().rstrip().split()))
    ans, stocks, best = 0, 0, 0
    for i in range(days):
        datum = prices.pop()
        if datum >= best:
            best = datum
        else:
            ans += (best - datum)
        
       
    print(ans)
from sys import stdin

expression = stdin.readline().rstrip().split('-')
answer = []
    
for i in expression:
    if '+' in i:
        temp = i.split('+')
        s = 0
        for j in temp:
            s += int(j)
        answer.append(s)
    else:
        answer.append(int(i))
        
ans = answer[0]
for i in answer[1::]:
    ans -= i

print(ans)
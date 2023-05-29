from sys import stdin
from collections import deque
import re

for _ in range(int(stdin.readline().rstrip())):
    functions = stdin.readline().rstrip()
    nums = int(stdin.readline().rstrip())
    dq = deque(list(map(int, re.findall(r'\d+',stdin.readline().rstrip()))))
    reversing = functions.count('R')
    
    a = list(functions.replace('D', ' D ').split())

    if functions.count('D') > nums:
        print('error')
    else:
        current_reversed = False

        for i in a:
            if i == 'D':
                if current_reversed == False:
                    dq.popleft()
                else:
                    dq.pop()
            else:
                if len(i) % 2 == 1:
                    if current_reversed == False:
                        current_reversed = True
                    else:
                        current_reversed = False  

        if reversing % 2 == 1:
            dq.reverse()
        
        temp = ','.join(str(s) for s in list(dq))
        print('[' + temp + ']')
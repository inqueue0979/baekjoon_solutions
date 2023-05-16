import sys
from collections import deque

cases = int(sys.stdin.readline().rstrip())
nums = deque()
comparison = deque(i for i in range(1, cases + 1))
answer = []
quit = False
a = 0

for _ in range(cases):
    num = int(sys.stdin.readline().rstrip())

    if quit == False:
        while True:
            
            if len(nums) == 0:
                a = nums.append(comparison.popleft())
                answer.append('+')
            else:
                if len(comparison) == 0 and nums[-1] != num:
                    print('NO')
                    quit = True
                    break
            
            if nums[-1] == num:
                answer.append('-')
                nums.pop()
                break
            else:
                a = nums.append(comparison.popleft())
                answer.append('+')

if quit == False:
    for i in answer:
        print(i)
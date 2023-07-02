from sys import stdin
from collections import deque
from copy import deepcopy

N, M = map(int, stdin.readline().rstrip().split())

l_queue = deque(list((i+1) for i in range(N)))
r_queue = deque(list((i+1) for i in range(N)))
answer = 0

locations = list(map(int, stdin.readline().rstrip().split()))

for i in locations:
    
    while True:

        if l_queue[0] == i:
            l_queue.popleft()
            r_queue = deepcopy(l_queue)
            break
        elif r_queue[0] == i:
            r_queue.popleft()
            l_queue = deepcopy(r_queue)
            break

        l_queue.append(l_queue.popleft())
        r_queue.appendleft(r_queue.pop())
        answer += 1

print(answer)
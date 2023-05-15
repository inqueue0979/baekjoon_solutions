import sys
from collections import deque

test_case = int(sys.stdin.readline().rstrip())

for _ in range(test_case):
    doc, num = map(int, sys.stdin.readline().rstrip().split())
    queue = deque((map(int, sys.stdin.readline().rstrip().split())))
    order = deque(i for i in range(doc))

    times = 0

    while True:
        if max(queue) != queue[0]:
            queue.append(queue.popleft())
            order.append(order.popleft())
        else:
            queue.popleft()
            a = order.popleft()
            times += 1

            if a == num:
                break

    print(times)
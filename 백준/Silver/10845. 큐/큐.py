import sys
from collections import deque

cases = int(sys.stdin.readline().rstrip())
nums = deque()
for i in range(cases):
    command = list(map(str, sys.stdin.readline().rstrip().split()))

    if command[0] == "push":
        nums.append(int(command[1]))
    elif command[0] == 'pop':
        if len(nums) == 0:
            print(-1)
        else:
            print(nums.popleft())
    elif command[0] == 'size':
        print(len(nums))
    elif command[0] == 'empty':
        if len(nums) == 0:
            print(1)
        else:
            print(0)
    elif command[0] == 'front':
        if len(nums) == 0:
            print(-1)
        else:
            print(nums[0])
    elif command[0] == 'back':
        if len(nums) == 0:
            print(-1)
        else:
            print(nums[-1])
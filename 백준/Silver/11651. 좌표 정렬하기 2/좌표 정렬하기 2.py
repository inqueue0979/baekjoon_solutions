import sys

num = int(sys.stdin.readline().rstrip())
nums = []

for i in range(num):
    nums.append(list(map(int, sys.stdin.readline().rstrip().split())))

nums.sort()
nums.sort(key= lambda x: x[1])

for i in nums:
    print(i[0], i[1])
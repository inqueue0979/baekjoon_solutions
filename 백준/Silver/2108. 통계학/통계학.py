import sys
import math
from collections import Counter

cases = int(sys.stdin.readline().rstrip())
nums = []
commons = []

for i in range(cases):
    nums.append(int(sys.stdin.readline().rstrip()))

nums.sort()

print(round(sum(nums) / cases)) #산술평균
print(nums[cases // 2]) #중앙값

common_times = Counter(nums).most_common()[0][1]

for i in Counter(nums).most_common():
    if i[1] == common_times:
        commons.append(i)

commons.sort()

if len(commons) > 1:
    print(commons[1][0])
else:
    print(commons[0][0])
    
print(max(nums) - min(nums)) #범위
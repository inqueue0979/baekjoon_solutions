from sys import stdin
nums = []
cases = int(stdin.readline().rstrip())

def banolim(data):
    return int(data) + 1 if data - int(data) >= 0.5 else int(data)

for _ in range(cases):
    nums.append(int(stdin.readline().rstrip()))

nums.sort()
jeolsa = banolim(cases * 0.15)

if cases != 0:
    print(banolim(sum(nums[jeolsa : cases - jeolsa]) / (cases - (jeolsa * 2))))
else:
    print(0)
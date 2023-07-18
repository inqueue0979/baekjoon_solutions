def DP(i, nums):

    if i > 3 and not nums.get(i, False):
        nums[i] = DP(i-1, nums) + DP(i-2, nums) + DP(i-3, nums)

    return nums[i]

from sys import stdin

nums = {1:1,
        2:2,
        3:4,
        4:7}

for _ in range(int(stdin.readline().rstrip())):
    print(DP(int(stdin.readline().rstrip()), nums))
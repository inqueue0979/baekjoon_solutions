from sys import stdin

_, K = map(int, stdin.readline().rstrip().split())
nums = sorted(list(map(int, stdin.readline().rstrip().split())))

print(nums[K-1])
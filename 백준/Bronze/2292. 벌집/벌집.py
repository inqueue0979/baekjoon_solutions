import sys

num = int(sys.stdin.readline().rstrip())
temp = 1
ans = 1

while num > temp:
    temp += 6 * ans
    ans += 1

print(ans)
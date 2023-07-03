from sys import stdin

levels = []
for _ in range(int(stdin.readline().rstrip())):
    levels.append(int(stdin.readline().rstrip()))

levels = levels[::-1]
answer = 0


for i in range(1, len(levels)):

    if levels[i-1] <= levels[i]:
        answer += levels[i] - levels[i-1] + 1
        levels[i] = levels[i - 1] - 1

print(answer)
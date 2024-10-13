from sys import stdin

cases = int(stdin.readline().rstrip())
data = list()
for i in range(cases):
    data.append(list(map(int, stdin.readline().rstrip().split())))

for y in range(1, cases):
    for x in range(y + 1):
        if x == 0:
            data[y][x] += data[y-1][x]
        elif x == y:
            data[y][x] += data[y-1][x-1]
        else:
            data[y][x] += max(data[y-1][x], data[y-1][x-1])

print(max(data[cases-1]))     
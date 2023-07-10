from sys import stdin

X = int(stdin.readline().rstrip())
answer = []

a = 0
temp = 1
rng = 0

while a < X:
    a += temp
    rng = temp
    temp += 4

if a - X + 1 > (rng - 1) // 2:
    answer.append(rng - (a - X))
else:
    answer.append(a - X + 1)

a = 0
temp = 3
rng = 0

while a < X:
    a += temp
    rng = temp
    temp += 4

if a - X + 1 > (rng - 1) // 2:
    answer.append(rng - (a - X))
else:
    answer.append(a - X + 1)

print(str(answer[0]) + '/' + str(answer[1]))
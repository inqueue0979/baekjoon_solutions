from sys import stdin

cases = int(stdin.readline().rstrip())
compare = stdin.readline().rstrip()
another = []
answer = []

for _ in range(cases - 1):
    another.append(stdin.readline().rstrip())

for i in range(len(compare)):
    for j in another:
        if compare[i] != j[i]:
            answer.append('?')
            break
    else:
        answer.append(compare[i])

print(''.join(answer))
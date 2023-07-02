from sys import stdin

count = int(stdin.readline().rstrip())
ropes = sorted([int(stdin.readline().rstrip()) for _ in range(count)], reverse=True)
answers = []

for _ in range(count):
    answers.append(ropes[-1] * len(ropes))
    ropes.pop()

print(max(answers))
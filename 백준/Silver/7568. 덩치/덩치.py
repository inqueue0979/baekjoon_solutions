import sys

case = int(sys.stdin.readline().rstrip())
height = []
weight = []
place = []

for i in range(case):
    w, h = map(int, sys.stdin.readline().rstrip().split())
    weight.append(w)
    height.append(h)

for i in range(case):
    score = 1

    for j in range(case):
        if height[i] < height[j] and weight[i] < weight[j]:
            score += 1
    
    place.append(score)

for i in range(case): print(place[i], end=' ')
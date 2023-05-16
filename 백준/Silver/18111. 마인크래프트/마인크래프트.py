from sys import stdin

N, M, B = map(int, stdin.readline().rstrip().split())
bestTime, highestHeight = 128000000, 0
ground = []

for _ in range(N):
    ground.extend(map(int, stdin.readline().rstrip().split()))

for height in range(min(ground), max(ground) + 1):

    time = 0
    blocks = B

    for i in ground:

        if i == height:
            pass
        elif i > height:
            time += ((i - height) * 2)
            blocks += (i - height)
        else:
            time += (height - i)
            blocks -= (height - i)

    if time <= bestTime and blocks >= 0:
        bestTime = time
        highestHeight = height


print(bestTime, highestHeight)
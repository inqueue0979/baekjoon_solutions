from sys import stdin

cases = int(stdin.readline().rstrip())
for _ in range(cases):
    x, y = map(int, stdin.readline().rstrip().split())
    dist = y - x

    mv = 1
    cnt = 0
    hap = 0

    while hap < dist:
        cnt += 1
        hap += mv

        if not cnt % 2:
            mv += 1
    print(cnt)
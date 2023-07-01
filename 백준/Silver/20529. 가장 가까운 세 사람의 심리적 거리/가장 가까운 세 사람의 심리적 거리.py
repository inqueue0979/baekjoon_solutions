from sys import stdin
from itertools import combinations

for _ in range(int(stdin.readline().rstrip())):
    nums = int(stdin.readline().rstrip())
    mbti = list(stdin.readline().rstrip().split())
    answer = 10000000000000000000

    if nums > 32:
        print(0)
        continue

    mbti_combi = combinations(mbti, 3)

    for mbtis in mbti_combi:
        temp = 0

        for i in range(3):
            for j in range(i + 1, 3):
                
                for k in range(4):
                    if mbtis[i][k] != mbtis[j][k]:
                        temp += 1

        if temp < answer:
            answer = temp
    
    print(answer)
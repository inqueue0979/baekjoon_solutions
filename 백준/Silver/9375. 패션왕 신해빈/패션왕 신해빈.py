from sys import stdin

test_case = int(stdin.readline().rstrip())

for _ in range(test_case):
    clothes = dict()
    nums = int(stdin.readline().rstrip())
    ans = 1

    for __ in range(nums):
        cloth, kind = stdin.readline().rstrip().split()

        if kind in clothes:
            clothes[kind] += 1
        else:
            clothes[kind] = 1

    for i in clothes:
       ans *= (clothes[i] + 1)

    print(ans - 1)
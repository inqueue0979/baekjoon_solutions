from sys import stdin

amp = {1:9,
       2:90 * 2,
       3:900 * 3,
       4:9000 * 4,
       5:90000 * 5,
       6:900000 * 6,
       7:9000000 * 7,
       8:90000000 * 8
}

a = int(stdin.readline().rstrip())
answer = 0

for i in range(1, len(str(a))):
    answer += amp[i]

print(answer + (a - ((10 ** (int(len(str(a))) - 1)) - 1)) * int(len(str(a))))
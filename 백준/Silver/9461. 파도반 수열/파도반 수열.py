from sys import stdin

padovan_list = [1, 1, 1]

for i in range(3, 100):
    padovan_list.append(padovan_list[i-2] + padovan_list[i-3])

for _ in range(int(stdin.readline().rstrip())):
    T = int(stdin.readline().rstrip())

    if T <= 3:
        print(1)
    else:
        print(padovan_list[T - 1])
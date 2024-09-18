from sys import stdin

buttons = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
target = int(stdin.readline().rstrip())
broken_nums = int(stdin.readline().rstrip())

if broken_nums != 0:
    broken = stdin.readline().rstrip().split()

    for i in broken:
        buttons.remove(i)

addsub = 0

while True:
    cursor_p = target + addsub
    cursor_m = target - addsub

    if cursor_m == 100:
        print(addsub)
        break
    else:
        for i in str(cursor_m):
            if i not in buttons:
                break
        else:
            print(min(abs(100 - target), addsub + len(str(cursor_m))))
            break

    if cursor_p == 100:
        print(addsub)
        break
    else:
        for i in str(cursor_p):
            if i not in buttons:
                break
        else:
            print(min(abs(100-target), addsub + len(str(cursor_p))))
            break

    addsub += 1
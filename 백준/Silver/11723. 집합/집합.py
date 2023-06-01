from sys import stdin

bit = 0b0

for _ in range(int(stdin.readline().rstrip())):
    a = stdin.readline().rstrip().split()

    if a[0] == 'add':
        bit |= (1 << int(a[1]))
    elif a[0] == 'remove':
        bit &= ~(1 << int(a[1]))
    elif a[0] == 'check':
        print(1 if bit & (1 << int(a[1])) != 0 else 0)
    elif a[0] == 'toggle':
        bit ^= (1 << int(a[1]))
    elif a[0] == 'all':
        bit = 0b111111111111111111111
    else: #empty
        bit = 0b0
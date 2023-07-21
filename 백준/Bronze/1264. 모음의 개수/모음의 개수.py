from sys import stdin

while True:
    a = stdin.readline().rstrip()
    moeum = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    ans = 0

    if a == '#':
        break

    for i in a:
        if i in moeum:
            ans += 1

    print(ans)
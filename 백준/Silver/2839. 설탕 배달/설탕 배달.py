a = int(input())
kg3 = 0
kg5 = 0

while True:

    if a % 5 == 0:
        kg5 = a / 5
        print(int(kg3 + kg5))
        break

    a = a - 3
    kg3 = kg3 + 1

    if a < 0:
        print(-1)
        break
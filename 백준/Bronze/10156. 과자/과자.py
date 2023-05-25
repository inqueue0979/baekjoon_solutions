import sys
chip, a, currency = map(int, sys.stdin.readline().rstrip().split())
print(chip * a - currency) if chip * a > currency else print(0)
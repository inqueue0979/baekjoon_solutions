from sys import stdin

while True:
    a = stdin.readline().rstrip()
    
    if a == "END":
        break

    print(a[::-1])
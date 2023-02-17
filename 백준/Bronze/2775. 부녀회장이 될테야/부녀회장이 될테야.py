import sys

cases = int(sys.stdin.readline().rstrip())

for tries in range(cases):

    cols = int(sys.stdin.readline().rstrip()) #세로 (층수)
    rows = int(sys.stdin.readline().rstrip()) #가로 (호수)


    arr = [[0 for j in range(rows)] for i in range(cols + 1)] #아파트 층수와 호수 고려해서 2차원 배열 만들기
    
    for k in range(0, rows): #0층에 사람 넣기
        arr[0][k] = k + 1

    for l in range(1, cols + 1):
        for m in range(0, rows):
            for n in range(0, m + 1):
                arr[l][m] = arr[l][m] + arr[l-1][n]

    print(arr[cols][rows - 1])
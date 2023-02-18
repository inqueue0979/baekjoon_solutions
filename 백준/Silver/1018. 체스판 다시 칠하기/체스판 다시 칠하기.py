import sys

N, M = map(int, sys.stdin.readline().rstrip().split())
chess = []
result = 2500

comparison = list()

for z in range(4):
    comparison.append(list('''BWBWBWBW'''))
    comparison.append(list('''WBWBWBWB'''))

for k in range(N):
    chess.append(list(sys.stdin.readline().rstrip()))

for column in range(0, N - 7):
    for row in range(0, M - 7):
        
        bres = 0
        wres = 0

        for vert in range(column, column + 8):
            for horiz in range(row, row + 8):

                if chess[vert][horiz] != comparison[vert - column][horiz-row]:
                    bres = bres + 1
                else:
                    wres = wres + 1

                #print(bres, wres)
                #print(vert, horiz)

        if bres > wres:
            if result > wres:
                result = wres
        elif bres <= wres:
            if result > bres:
                result = bres

print(result)
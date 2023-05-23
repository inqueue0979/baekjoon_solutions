from sys import stdin

init_game = [['.' for _ in range(6)] for _ in range(6)]
init_game[2] = ['.','.','W','B','.','.']
init_game[3] = ['.','.','B','W','.','.']
direction = [[0, 1], [0, -1], [1, 0], [-1, 0], [1, 1], [1, -1], [-1, 1], [-1, -1]]

num = int(stdin.readline().rstrip())
board = init_game
black, white = 0, 0

for i in range(num):
    row, col = map(int, stdin.readline().rstrip().split())
    row -= 1
    col -= 1
    current = ''

    if i % 2 == 0:
        current = 'B'
    else:
        current = 'W'
    
    board[row][col] = current

    for dir_y, dir_x in direction:
        dir_row, dir_col = row, col
        trace = []

        while True:

            dir_row += dir_y
            dir_col += dir_x

            if dir_row > 5 or dir_col > 5 or dir_row < 0 or dir_col < 0:
                break

            trace.append([dir_row, dir_col])

            if board[dir_row][dir_col] == '.':
                break
            
            elif board[dir_row][dir_col] == current:

                for change_y, change_x in trace:
                    board[change_y][change_x] = current

                break
    
for i in range(6):
    for j in range(6):
        print(board[i][j], end='')
    print()

for i in range(6):
    black += board[i].count('B')
    white += board[i].count('W')

print('Black') if black > white else print('White')
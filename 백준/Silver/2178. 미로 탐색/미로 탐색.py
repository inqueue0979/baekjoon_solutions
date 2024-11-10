from collections import deque

def BFS(graph, start_x, start_y, max_x, max_y, visited, ans):
    queue = deque()
    queue.append((start_x, start_y))
    visited[start_x][start_y] = True
    ans[start_x][start_y] = 1

    direction = [(1, 0), (-1, 0), (0, 1), (0, -1)]

    while queue:
        node_x, node_y = queue.popleft()
        
        for dir_x, dir_y in direction:
            next_x = node_x + dir_x
            next_y = node_y + dir_y
            
            if 0 <= next_x < max_x and 0 <= next_y < max_y:
                if graph[next_x][next_y] == 1 and not visited[next_x][next_y]:
                    visited[next_x][next_y] = True
                    ans[next_x][next_y] = ans[node_x][node_y] + 1
                    queue.append((next_x, next_y))

from sys import stdin
N, M = map(int, stdin.readline().rstrip().split())
maze = []

for _ in range(N):
    row = stdin.readline().rstrip()
    maze.append(list(map(int, row)))  # 문자열을 정수로 변환
visited = [[False] * M for _ in range(N)]
ans = [[0] * M for _ in range(N)]

BFS(maze, 0, 0, N, M, visited, ans)

print(ans[N - 1][M - 1])
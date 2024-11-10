from collections import deque

def ms_BFS(graph, startings, max_x, max_y, visited, ans):
    queue = deque()
    
    # 모든 시작점을 큐에 넣고 초기화
    for start_x, start_y in startings:
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
                if graph[next_x][next_y] == 0 and not visited[next_x][next_y]:
                    visited[next_x][next_y] = True
                    ans[next_x][next_y] = ans[node_x][node_y] + 1
                    queue.append((next_x, next_y))

# 입력 처리
from sys import stdin
M, N = map(int, stdin.readline().rstrip().split())
maze = []

for _ in range(N):
    maze.append(list(map(int, stdin.readline().rstrip().split())))  # 문자열을 정수로 변환

visited = [[False] * M for _ in range(N)]
ans = [[0] * M for _ in range(N)]
startings = []

# 시작 지점 수집
for y in range(N):
    for x in range(M):
        if maze[y][x] == 1:
            startings.append((y, x))

# 멀티 소스 BFS 호출
ms_BFS(maze, startings, N, M, visited, ans)

# 결과 계산
max_num = 0
for y in range(N):
    for x in range(M):
        if ans[y][x] > max_num:
            max_num = ans[y][x]

for y in range(N):
    for x in range(M):
        if not visited[y][x] and maze[y][x] == 0:
            max_num = 0
            break

print(max_num - 1)